import os
import torch
import numpy as np
import argparse
from os.path import join as pjoin

import util.paramUtil as paramUtil
from torch.utils.data import DataLoader
from util.plot_script import *
from util.get_opt import get_opt
from datasets.evaluator_models import MotionLenEstimatorBiGRU

from trainers import DDPMTrainer
from trans.transformer import MotionTransformer
from util.word_vectorizer import WordVectorizer, POS_enumerator
from util.utils import *
from util.motion_process import recover_from_ric
import json

def plot_t2m(data, result_path, npy_path, caption):
    
    print(data)
    #joint = recover_from_ric(torch.from_numpy(data).float(), opt.joints_num).numpy()
    #joint = motion_temporal_filter(joint, sigma=1)
    #plot_3d_motion(result_path, paramUtil.t2m_kinematic_chain, joint, title=caption, fps=20)
    if npy_path != "":
        print(npy_path, flush=True)
        np.save(npy_path, data)


def build_models(opt):
    encoder = MotionTransformer(
        input_feats=opt.dim_pose,
        num_frames=opt.max_motion_length,
        num_layers=opt.num_layers,
        latent_dim=opt.latent_dim,
        no_clip=opt.no_clip,
        no_eff=opt.no_eff)
    return encoder


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--opt_path', type=str, help='Opt path')
    parser.add_argument('--text', type=str, default="", help='Text description for motion generation')
    parser.add_argument('--motion_length', type=int, default=60, help='Number of frames for motion generation')
    parser.add_argument('--result_path', type=str, default="test_sample.gif", help='Path to save generation result')
    parser.add_argument('--npy_path', type=str, default="", help='Path to save 3D keypoints sequence')
    parser.add_argument('--gpu_id', type=int, default=-1, help="which gpu to use")
    args = parser.parse_args()
    
    device = torch.device('cuda:%d' % args.gpu_id if args.gpu_id != -1 else 'cpu')
    opt = get_opt(args.opt_path, device)
    opt.do_denoise = True

    #assert opt.dataset_name == "t2m"
    #assert args.motion_length <= 196
    #opt.data_root = './dataset/HumanML3D'
    #opt.motion_dir = pjoin(opt.data_root, 'new_joint_vecs')
    #opt.text_dir = pjoin(opt.data_root, 'texts')
    #opt.joints_num = 22
    #opt.dim_pose = 263
    #dim_word = 300
    #dim_pos_ohot = len(POS_enumerator)
    #num_classes = 200 // opt.unit_length


    opt.data_root = '/content/drive/MyDrive/dataFolder/final'
    opt.motion_dir = pjoin(opt.data_root, 'landmarks')
    opt.text_dir = pjoin(opt.data_root, 'text')
    opt.joints_num = 21
    opt.dim_pose = 42
    dim_word = 300
    dim_pos_ohot = len(POS_enumerator)
    num_classes = 200 // opt.unit_length

    mean = np.load(pjoin(opt.meta_dir, 'mean.npy'))
    std = np.load(pjoin(opt.meta_dir, 'std.npy'))

    encoder = build_models(opt).to(device)
    trainer = DDPMTrainer(opt, encoder)
    trainer.load(pjoin(opt.model_dir, opt.which_epoch + '.tar'))

    trainer.eval_mode()
    trainer.to(opt.device)

    result_dict = {}
    with torch.no_grad():
        if args.motion_length != -1:
            if args.text.endswith(".json"):
                with open(args.text) as json_file:
                    testSet=json.load(json_file)

                count=0
                for i in testSet:
                    input=i.split("#")[0]
                    caption = [input]
                    #m_lens = torch.LongTensor([args.motion_length]).to(device)
                    m_lens=torch.LongTensor([testSet[i]["length"]-1]).to(device)
                    pred_motions = trainer.generate(caption, m_lens, opt.dim_pose)
                    motion = pred_motions[0].cpu().numpy()
                    motion = motion * std + mean
                    testSet[i]["output"]=motion.tolist()
                    if count%10==0:
                        with open("/content/drive/MyDrive/Output/"+str(args.result_path),"w") as output_file:
                            json.dump(testSet,output_file)
                        output_file.close()
                    count=count+1
                    #title = args.text + " #%d" % motion.shape[0]
                    #plot_t2m(motion, args.result_path, args.npy_path, title)s
                with open("/content/drive/MyDrive/Output/"+str(args.result_path),"w") as output_file:
                    json.dump(testSet,output_file)
                output_file.close()

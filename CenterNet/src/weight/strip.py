import torch
import os

def strip_optimizer(f='weight/best.pt', s=''):  # from utils.general import *; strip_optimizer()
    # Strip optimizer from 'f' to finalize training, optionally save as 's'
    x = torch.load(f, map_location=torch.device('cpu'))
    # print(x.keys())
    # #print(x['epoch'])#安全
    # #print(x['best_fitness'])  # [    0.57436] 不重要
    #
    model = x['model']
    print(model.names)
    # model.names = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]
    # print(type(model))
    # #print(x['optimizer'])#None
    # #print(x['training_results']) #None

    x['optimizer'] = None
    x['training_results'] = None
    x['epoch'] = -1
    x['model'].half()  # to FP16
    x['best_fitness'] = None
    for p in x['model'].parameters():
        #print(p)
        p.requires_grad = False
    torch.save(x, s or f)
    mb = os.path.getsize(s or f) / 1E6  # filesize
    print('Optimizer stripped from %s,%s %.1fMB' % (f, (' saved as %s,' % s) if s else '', mb))

def strip_optimizer_pth_with_no_model(f='weight/best.pt', s=''):  # from utils.general import *; strip_optimizer()
    # Strip optimizer from 'f' to finalize training, optionally save as 's'
    x = torch.load(f, map_location=torch.device('cpu'))
    # print(x.keys())
    # #print(x['epoch'])#安全
    # #print(x['best_fitness'])  # [    0.57436] 不重要
    #
    print(x.keys())
    # model = x['model']
    # print(model.names)
    # model.names = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19"]
    # print(type(model))
    # #print(x['optimizer'])#None
    # #print(x['training_results']) #None

    x['optimizer'] = None
    x['training_results'] = None
    x['epoch'] = -1
    # x['model'].half()  # to FP16
    x['best_fitness'] = None
    # for p in x['model'].parameters():
    #     #print(p)
    #     p.requires_grad = False
    torch.save(x, s or f)
    mb = os.path.getsize(s or f) / 1E6  # filesize
    print('Optimizer stripped from %s,%s %.1fMB' % (f, (' saved as %s,' % s) if s else '', mb))


strip_optimizer('test/4pre.pt','test/out_4pre.pt')


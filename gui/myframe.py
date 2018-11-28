# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.2 on Tue Aug 21 13:46:28 2018
#

import wx
import wx.aui
import os
import sys
import gettext
_ = gettext.gettext
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
from mynotebook import MyNotebook
from utils.util import Redirection, pickle_load

from run import Run
from run import get_model_list, get_data_list, get_optimizer_list

os.environ["UBUNTU_MENUPROXY"] = "0"

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1194, 922))

        self.cwd = os.getcwd()

        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Import"), "")
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Export"), "")
        self.frame_menubar.Append(wxglade_tmp_menu, _("File"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Create"), "")
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Load"), "")
        self.frame_menubar.Append(wxglade_tmp_menu, _("Datasets"))
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Train Spec"), "")
        wxglade_tmp_menu.Append(wx.ID_ANY, _("Test Spec"), "")
        #wxglade_tmp_menu.Append(wx.ID_ANY, _("Run"), "")
        self.frame_menubar.Append(wxglade_tmp_menu, _("Models"))
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end

        # Tool Bar
        self.tool_bar = wx.ToolBar(self, wx.ID_ANY)
        self.SetToolBar(self.tool_bar)
        self.tool_new = self.tool_bar.AddTool(1, _("New"), wx.Bitmap("./icons/add.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("New"), "")
        self.tool_load = self.tool_bar.AddTool(2, _("Load"), wx.Bitmap("./icons/upload.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Load"), "")
        self.tool_save = self.tool_bar.AddTool(3, _("Save"), wx.Bitmap("./icons/diskette(1).png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Save"), "")
        self.tool_bar.AddSeparator()
        self.tool_train_spec = self.tool_bar.AddTool(4, _("Train Spec"), wx.Bitmap("./icons/3d-modeling.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Train Spec"), "")
        self.tool_run = self.tool_bar.AddTool(5, _("Run"), wx.Bitmap("./icons/play(1).png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Run"), "")
        self.tool_bar.AddSeparator()
        self.tool_test = self.tool_bar.AddTool(6, _("Test"), wx.Bitmap("./icons/background.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, _("Test"), "")
        self.tool_bar.EnableTool(self.tool_run.GetId(), False)
        # Tool Bar end

        # TreeCtrl
        self.data_tree = self.tree_ctrl_1 = wx.TreeCtrl(self, wx.ID_ANY)#, style=wx.BORDER_SUNKEN | wx.TR_HAS_BUTTONS)
        self.model_tree = self.tree_ctrl_2 = wx.TreeCtrl(self, wx.ID_ANY)#, style=wx.BORDER_SUNKEN | wx.TR_HAS_BUTTONS)
        self.item_to_page = dict()

        # load dataset tree
        self.datasetDir = os.path.join(self.cwd, "Dataset")
        if not os.path.exists(self.datasetDir):
            os.makedirs(self.datasetDir)
        # data folder tree
        self.buildTree(self.data_tree, self.datasetDir)
        # open data
        self.appendTree(self.data_tree, self.data_tree.GetRootItem(), get_data_list())
        self.data_tree.Expand(self.data_tree.GetRootItem())

        # load model tree (in Modules folder)
        self.modelDir = os.path.join(self.cwd, "model")
        self.buildTree(self.model_tree, self.modelDir)
        # model library
        self.appendTree(self.model_tree, self.model_tree.GetRootItem(), get_model_list(), model=True)
        self.model_tree.Expand(self.model_tree.GetRootItem())

#        # load pretrained model tree (in checkpoint folder)
#        self.pretrainedModelDir = os.path.join(self.cwd, "checkpoint")
#        if os.path.exists(self.pretrainedModelDir):
#            for pretrainedModel in os.listdir(self.pretrainedModelDir):
#                pretrainedModelPath = os.path.join(self.pretrainedModelDir, pretrainedModel)
#                self.buildTree(self.model_tree, pretrainedModelPath)
#            self.model_tree.Expand(self.model_tree.GetRootItem())

        # toList
        #self.dataset_list = self.childrenToList(self.data_tree, self.data_tree.GetRootItem())
        #self.model_list = self.childrenToList(self.model_tree, self.model_tree.GetRootItem())
        # TreeCtrl end

        # AuiNotebook
        self.notebook = self.notebook_1 = MyNotebook(self, wx.ID_ANY)
        # AuiNotebook end

        # log window
        self.text_log = self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "log\n", style=wx.HSCROLL | wx.TE_LEFT | wx.TE_MULTILINE | wx.TE_READONLY)
        self.redir = Redirection(self.text_log)
        sys.stdout = self.redir
        # log window end

        self.__set_properties()
        self.__do_layout()
        self.__do_binds()
        # end wxGlade


    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(_("Tensorflow GUI"))
        self.tool_bar.Realize()
        self.text_ctrl_1.SetBackgroundColour(wx.Colour(235, 235, 235))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(self.tree_ctrl_1, 1, wx.EXPAND | wx.BOTTOM, 5)
        sizer_3.Add(self.tree_ctrl_2, 1, wx.EXPAND | wx.TOP, 5)
        sizer_2.Add(sizer_3, 2, wx.EXPAND, 0)
        sizer_2.Add(self.notebook_1, 5, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 4, wx.EXPAND, 0)
        sizer_1.Add(self.text_ctrl_1, 2, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def __do_binds(self):
        # tool bar
        self.tool_bar.Bind(wx.EVT_TOOL, self.OnNew, id=self.tool_new.GetId())
        self.tool_bar.Bind(wx.EVT_TOOL, self.OnLoad, id=self.tool_load.GetId())
        self.tool_bar.Bind(wx.EVT_TOOL, self.OnSave, id=self.tool_save.GetId())
        self.tool_bar.Bind(wx.EVT_TOOL, self.OnTrainSpec, id=self.tool_train_spec.GetId())
        self.tool_bar.Bind(wx.EVT_TOOL, self.OnRun, id=self.tool_run.GetId())
        self.tool_bar.Bind(wx.EVT_TOOL, self.OnTestSpec, id=self.tool_test.GetId())

        # trees
        self.data_tree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.dataTreeOnActivated)
        self.model_tree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.modelTreeOnActivated)
        self.data_tree.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.dataTreeOnExpand)
        self.model_tree.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.modelTreeOnExpand)

        # notebook
        self.notebook.Bind(wx.lib.agw.aui.auibook.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnPageChanged)

    def OnClosed(self, event):
        print('closed')
    def OnPageChanged(self, event):
        if self.notebook.isOnTrainSpec() or self.notebook.isOnTestSpec():
            self.tool_bar.EnableTool(self.tool_run.GetId(), True)
        else:
            self.tool_bar.EnableTool(self.tool_run.GetId(), False)
    def dataTreeOnExpand(self, event):
        itemID = event.GetItem()
        self.data_tree.DeleteChildren(itemID)
        self.extendTree(self.data_tree, itemID)
        if self.data_tree.GetItemData(itemID) is \
                self.data_tree.GetItemData(self.data_tree.GetRootItem()):
            self.appendTree(self.data_tree, self.data_tree.GetRootItem(), get_data_list())
    def modelTreeOnExpand(self, event):
        itemID = event.GetItem()
        self.model_tree.DeleteChildren(itemID)
        self.extendTree(self.model_tree, itemID)
        if self.model_tree.GetItemData(itemID) is \
                self.model_tree.GetItemData(self.model_tree.GetRootItem()):
            self.appendTree(self.model_tree, self.model_tree.GetRootItem(), get_model_list(), True)
    def refresh_trees(self):
        self.data_tree.DeleteChildren(self.data_tree.GetRootItem())
        self.extendTree(self.data_tree, self.data_tree.GetRootItem())
        self.appendTree(self.data_tree, self.data_tree.GetRootItem(), get_data_list())
        self.data_tree.Expand(self.data_tree.GetRootItem())

        self.model_tree.DeleteChildren(self.model_tree.GetRootItem())
        self.extendTree(self.model_tree, self.model_tree.GetRootItem())
        self.appendTree(self.model_tree, self.model_tree.GetRootItem(), get_model_list(), True)
        self.model_tree.Expand(self.model_tree.GetRootItem())


    def OnToolBar(self, event):
        print(event)
        print(event.GetInt())
    def OnNew(self, event):
        pass
    def OnLoad(self, event):
        pass
    def OnSave(self, event):
        pass

    def OnTestSpec(self, event):
        test_spec = self.getTestSpec()
        ### return dict
        ### model_list, model_names, trained_model_list_names
        page = self.notebook.createTestSpecPanel(self.notebook, wx.ID_ANY)
        page.setTestSpec(test_spec)

    def OnTrainSpec(self, event):
        train_spec = self.getTrainSpec()
        ### return dict
        ### max_epochs, learning_rate, seed, batch_size, interval,
        ### learning_rate, dataset_list, model_list, dataset_names, model_names,
        ### trained_model_dict, trained_model_names_dict, checkpoint_name, solver_list
        page = self.notebook.createTrainSpecPanel(self.notebook, wx.ID_ANY)
        page.setTrainSpec(train_spec)

    def OnRun(self, event):
        args = {}
        page, phase, spec = self.notebook.getRunSpec()
        args['page'], args['phase'] = page, phase
        args.update(spec)
        ### return page, phase, spec
        ###             (train): model_name, dataset_name, gpu, trained_model_name, checkpoint_name,
        ###                     max_ecpochs, batch_size, optimizer, learning_rate, interval, speed
        ###
        ###             (test): model_name, upload_list

        if spec is not None:
            if phase == 'Train':
                assert spec['dataset_name']
                datasetID = self.getDataDict()[spec['dataset_name']]
                dataset_spec = self.getDataSpec(datasetID)
                
                if spec['trained_model_name'] is None:
                    modelID = self.getModelsDict()[0][spec['model_name']]
                    #modelID = page.train_spec['model_list'][page.train_spec['model_names'].index(args['dataset_name'])]
                else:
                    modelID = self.getModelsDict()[1][spec['model_name']][spec['data_name']][spec['trained_model_name']]
                    #modelID = page.train_spec['trained_model_dict'][args['model_name']]
                model_spec = self.getModelSpec(modelID)

            elif phase == 'Test':
                dataset_spec = self.getTestDataSpec(spec['upload_list'])
                modelID = self.getModelsDict()[1][spec['model_name']][spec['data_name']][spec['trained_model_name']]
                model_spec = self.getModelSpec(modelID)
                args.update({'gpu':"cpu"})

            args['model_spec'] = model_spec
#            args['model_spec'] = self.getModelSpec(modelID)
            """
            return {'name',
                    'path',
                    'trained':pickle_load,
                    'type':'None',
                    'n_layer':'None',
                    'input_size':'None',
                    'output_size':'None'}
            """
            args['dataset_spec'] = dataset_spec 
#            args['dataset_spec'] = self.getDataSpec(datasetID)
            """
            data_spec['name']
            data_spec['path']
            data_spec['label_names']
            data_spec['data']
            data_spec['output_size']
            data_spec['input_types']
            data_spec['input_shapes']
            """

            #print(args.keys())
            #print(dataset_spec.keys())
            #print(dataset_spec['data'].keys())
            #print(model_spec)
            #print(model_spec.keys())
#        self.model_name, self.dataset_name, gpu_selected, \
        #        self.checkpoint, self.epochs, self.batch_size, self.optimizer, \
        #        self.learning_rate, self.interval, self.random_seed \
        #        self.input_shape, self.output_size = spec[1:]

#            print("\nrun args\n", args.keys())
#            def keys(d):
#                for k, v in d.items():
#                    if isinstance(v, dict):
#                        print(k, v.keys())
#                        keys(v)
#            keys(args)
#            print("\n")
            Run(**args)
            self.refresh_trees()
            pass


            return Run(**args)
        else:
            # self.tool_bar.EnableTool(self.tool_run.GetId(), False)
            pass

    def OnDataSpec(self, item):
        data_spec = self.getDataSpec(item)
#        import numpy as np
#        print(np.array(data_spec))
        if data_spec is None:
            print('wrong dataset folder')
            return
        page = self.notebook.createDataSpecPanel(self.notebook, wx.ID_ANY)
        page.setDataSpec(data_spec)

        self.item_to_page[item] = page

    def OnModelSpec(self, item):
        model_spec = self.getModelSpec(item)
        page = self.notebook.createModelSpecPanel(self.notebook, wx.ID_ANY)
        page.setModelSpec(model_spec)

        self.item_to_page[item] = page

    def OnTrainedSpec(self, item):
        trained_spec = self.getTrainSpec()
        trained_spec.update(self.getModelSpec(item))
        page = self.notebook.createTrainSpecPanel(self.notebook, wx.ID_ANY)
        page.setTrainSpec(trained_spec)

        self.item_to_page[item] = page

    def isDataset(self, item):
        return self.data_tree.GetItemParent(item) == \
                self.data_tree.GetRootItem()

    def treeOnActivated(self, tree, OnSpecFun):
        #print('TreeOnActivated')
        item = tree.GetFocusedItem()

        if tree.GetItemParent(item) == tree.GetRootItem():
            if item not in self.item_to_page:
                OnSpecFun(item)
            else:
                _, idx = self.notebook.FindTab(self.item_to_page[item])
                if idx == -1:
                    OnSpecFun(item)
                else:
                    self.notebook.SetSelection(idx)

    def dataTreeOnActivated(self, event):
        #self.treeOnActivated(self.data_tree, self.OnDataSpec)
        tree, OnSpecFun = self.data_tree, self.OnDataSpec
        item = tree.GetFocusedItem()

        if tree.GetItemParent(item) == tree.GetRootItem():
            if item not in self.item_to_page:
                OnSpecFun(item)
            else:
                _, idx = self.notebook.FindTab(self.item_to_page[item])
                if idx == -1:
                    OnSpecFun(item)
                else:
                    self.notebook.SetSelection(idx)


    def modelTreeOnActivated(self, event):
        #self.treeOnActivated(self.model_tree, self.OnModelSpec)
        tree = self.model_tree 
        item = tree.GetFocusedItem()
        root = tree.GetRootItem()
        Parent = lambda x: tree.GetItemParent(x)

        if item != root:
            if Parent(item) == root:
                OnSpecFun = self.OnModelSpec
            elif Parent(Parent(Parent(item))) == root:
                #OnSpecFun = self.OnModelSpec
                OnSpecFun = self.OnTrainedSpec
            else:
                return

            if item not in self.item_to_page:
                OnSpecFun(item)
            else:
                _, idx = self.notebook.FindTab(self.item_to_page[item])
                if idx == -1:
                    OnSpecFun(item)
                else:
                    self.notebook.SetSelection(idx)

    def getTrainDataSpec(self, dirpath):
        pass

    def getTestDataSpec(self, paths):
        data_spec = dict()
        #data_spec['path'] = paths
        ######################################################
        # Fix it if we can deal with various data in general.
        data_spec['data_type'] = 'I' # image
        data_spec['valid_rate'] = 0.05 # validation ratio
        ######################################################

        data_spec['data'] = {'train':{'x':[], 'y':[]}, 'test':{'x':[], 'y':[]}}
        #print("case 4")
        for path in paths:
            if os.path.isdir(path):
                child = [os.path.join(path, child) for child in os.listdir(path)]
                data_spec_ = self.getTestDataSpec(child)
                data_spec.update(data_spec_)
            else:
                data_spec['data']['test']['x'] += [path]
        from PIL import Image

        #data = np.concatenate((train[:,0], test[:,0]), axis=0)
        x_data = data_spec['data']['test']['x']
        
        types = []
        input_shapes = []
        for x in x_data:
            fname, ext = os.path.splitext(x)
            if ext not in types:
                types.append(ext)

            if ext == '.png' or ext == '.jpg':
                img = Image.open(x)
                input_shape = img.size
                if input_shape not in input_shapes:
                    input_shapes.append(input_shape)
            else:
                print("We don't support type %s in %s"%(ext, x))
                data_spec['data']['test']['x'].remove(x)

        data_spec['input_types'] = types
        data_spec['input_shapes'] = input_shapes

        return data_spec

    def getDataSpec(self, dataID):
        #TODO : how about data aggregated into a single file like .csv, .txt, etc.
        # return name, path, data_type, valid_rate,
        #       label_names, data, output_size, input_types, input_shapes
        import numpy as np

        data_spec = dict()
        data_name = self.data_tree.GetItemText(dataID)
        data_path = self.data_tree.GetItemData(dataID)
        data_spec['name'] = data_name
        data_spec['path'] = data_path

        if not data_path in get_data_list():
            ######################################################
            # Fix it if we can deal with various data in general.
            data_spec['data_type'] = 'I' # image
            ######################################################
        else:
            data_info = get_data_list(data_name)(meta=True)
            ######################################################
            # Open data setting
            data_spec['path'] = 'Open Data'
            data_spec['data_type'] = data_info['data_type']
            data_spec['label_names'] = str(data_info['label_names'])
            data_spec['data'] = {'train':{'x':np.zeros(data_info['ntrain'])}, 'test':{'x':np.zeros(data_info['ntest'])}}
            data_spec['output_size'] = str(data_info['classes'])
            t = data_info['data_type']
            data_spec['input_types'] = 'Image' if t == 'I' else 'Point' if t == 'P' else 'Time-serise' if t == 'T' else 'Unknown'
            data_spec['input_shapes'] = str(data_info['input_shape'])[1:-1]
            return  data_spec
            ######################################################

        data_spec['valid_rate'] = 0.05 # validation ratio


        childs = os.listdir(data_path)
        # Data/, train.txt, test.txt
        if 'Data' in childs and 'train.txt' in childs and 'test.txt' in childs:
            #print('case1')
            path_fun = lambda a: [data_path+'/'+a[0]] + a[1:] # data_file, label
            with open(os.path.join(data_path, 'train.txt'), 'r') as f:
                train = np.array([path_fun(x.split()) for x in f.read().splitlines()])
                x_train = train[:,0]
                y_train = train[:,1]
            with open(os.path.join(data_path, 'test.txt'), 'r') as f:
                test = np.array([path_fun(x.split()) for x in f.read().splitlines()])
                x_test = test[:,0]
                y_test = test[:,1]
            label_names = [str(label) for label in np.unique(y_train.tolist() + y_test.tolist())]

            train, test = {}, {}
            train['x'], test['x'] = np.array(x_train), np.array(x_test)
            train['y'] = np.array(list(map(lambda x: label_names.index(x), y_train)))
            test['y'] = np.array(list(map(lambda x: label_names.index(x), y_test)))
        # train/, test/, labels.txt
        elif 'train' in childs and 'test' in childs and 'labels.txt' in childs:
            #print('case2')
            with open(os.path.join(data_path, 'labels.txt'), 'r') as f:
                label_names = np.array(f.read().splitlines())

            #x_train = os.listdir(os.path.join(data_path, 'train'))
            x_train = [os.path.join(data_path, 'train', data) for data in os.listdir(os.path.join(data_path, 'train'))]
            y_train = np.zeros(len(x_train))
            trainpath_fun = lambda a: [data_path+a[0]] + a[1:]
            for i, x in enumerate(x_train):
                label_check = False
                for label, label_name in enumerate(label_names):
                    if label_name in x:
                        label_check = True
                        y_train[i] = label
                if not label_check:
                    print("Data without label %s"%x)
            train = {}
            train['x'] = np.array(x_train)
            train['y'] = np.array(y_train, int)
            #train = np.concatenate(([x_train], [y_train]), axis=0).T

            #x_test = os.listdir(os.path.join(data_path, 'test'))
            x_test = [os.path.join(data_path, 'test', data) for data in os.listdir(os.path.join(data_path, 'test'))]
            y_test = np.zeros(len(x_test))
            for i, x in enumerate(x_test):
                label_check = False
                for label, label_name in enumerate(label_names):
                    if label_name in x:
                        label_check = True
                        y_test[i] = label
                if not label_check:
                    print("Data without label %s"%x)

            test = {}
            test['x'] = np.array(x_test)
            test['y'] = np.array(y_test, int)
            #test = np.concatenate(([x_test], [y_test]), axis=0).T

        # [label]/, ... , train.txt, test.txt
        elif 'train.txt' in childs and 'test.txt' in childs:
            #print('case3')
            label_names = np.sort([ label for label in childs if os.path.isdir(os.path.join(data_path, label)) ])
#            print(label_names)
#            label_names = [ label for label in childs if os.path.isdir(os.path.join(data_path, label)) ]
#            print(label_names)

            with open(os.path.join(data_path, 'train.txt'), 'r') as f:
                x_train = f.read().splitlines()
#                x_train = [os.path.join(data_path, f.read().splitlines()]
                y_train = np.zeros(len(x_train))
                for i, x in enumerate(x_train):
                    label_check = False
                    for label, label_name in enumerate(label_names):
                        if label_name in x:
                            label_check = True
                            x_train[i] = os.path.join(data_path, x_train[i])
                            y_train[i] = label
                    if not label_check:
                        print("Data without label %s"%x)
            train = {}
            train['x'] = np.array(x_train)
            train['y'] = np.array(y_train, int)
            #train = np.concatenate(([x_train], [y_train]), axis=0).T

            with open(os.path.join(data_path, 'test.txt'), 'r') as f:
                #test = f.read().splitlines()
                x_test = f.read().splitlines()
                y_test = np.zeros(len(x_test))
                for i, x in enumerate(x_test):
                    label_check = False
                    for label, label_name in enumerate(label_names):
                        if label_name in x:
                            label_check = True
                            x_test[i] = os.path.join(data_path, x_test[i])
                            y_test[i] = label
                    if not label_check:
                        print("Data without label %s"%x)
            test = {}
            test['x'] = np.array(x_test)
            test['y'] = np.array(y_test, int)
            #test = np.concatenate(([x_test], [y_test]), axis=0).T

        else:
            dial = wx.MessageDialog(None, 'Invalid Dataset folder \n%s'%data_path, 'Error',
                wx.OK | wx.ICON_ERROR)
            dial.ShowModal()
            self.data_tree.Delete(dataID)
            assert False, 'Invalid Dataset folder %s'%data_path

        data_spec['label_names'] = label_names
        data_spec['data'] = {'train':train, 'test':test}
        data_spec['output_size'] = str(len(label_names))

        from PIL import Image

        #data = np.concatenate((train[:,0], test[:,0]), axis=0)
        x_data = np.concatenate([data['x'] for data in data_spec['data'].values()], axis=0)

        types = []
        input_shapes = []
        for x in x_data:
            fname, ext = os.path.splitext(x)
            if ext not in types:
                types.append(ext)

            if ext == '.png' or ext == '.jpg':
                img = np.array(Image.open(x))
                input_shape = str(img.shape)[1:-1]
                if input_shape not in input_shapes:
                    input_shapes.append(input_shape)
            else:
                print("We don't support type %s"%ext)

        data_spec['input_types'] = types
        data_spec['input_shapes'] = input_shapes

        return data_spec

    def getModelSpec(self, modelID):
        spec = {}
        dataID = self.model_tree.GetItemParent(modelID)
        name = self.model_tree.GetItemText(modelID)
        path = self.model_tree.GetItemData(modelID)
        trained = pickle_load(os.path.join(path, "meta")) \
            if os.path.exists(os.path.join(path, "meta.pickle")) else \
            None 
            
        spec['name'] = name
        spec['path'] = path
        if trained is not None:
            spec['trained'] = trained
            moduleID = self.model_tree.GetItemParent(dataID)
            model_name = self.model_tree.GetItemText(moduleID)
            spec['model_name'] = model_name
        spec.update({'type':'None',
            'n_layer':'None',
            'input_size':'None',
            'output_size':'None'})
        #print(spec)
        return spec
#    def setModelSpec(self):
#        pass

    def getTrainSpec(self):
        ### return dict
        ### max_epochs, learning_rate, seed, batch_size, interval, checkpoint_name, solver_list,
        ### dataset_dict, model_dict, trained_model_dict
        train_spec = {'max_epochs': '10000', 'learning_rate':'1e-3', 'seed':'0', 'batch_size':'32', 'interval':'.1', \
                'checkpoint_name': "checkpoint", "solver_list":get_optimizer_list()}

        train_spec['dataset_dict'] = self.getDataDict()
        train_spec['model_dict'], train_spec['trained_model_dict'] = self.getModelsDict()
        return train_spec
        
        ### return dict
        ### max_epochs, learning_rate, seed, batch_size, interval,
        ### learning_rate, dataset_list, model_list, dataset_names, model_names,
        ### trained_model_dict, trained_model_names_dict, checkpoint_name, solver_list
        train_spec = {'max_epochs': '10000', 'learning_rate':'1e-3', 'seed':'0', 'batch_size':'32', 'interval':'1000'}
        train_spec['dataset_dict'] = {}
        for ID in self.childrenToList(self.data_tree, self.data_tree.GetRootItem()):
            name = self.data_tree.GetItemText(ID)
            train_spec['data_dict'][name] = ID

        train_spec['model_dict'] = {}
        train_spec['trained_model_dict'] = {}
        for ID in self.childrenToList(self.model_tree, self.model_tree.GetRootItem()):
            name = self.model_tree.GetItemText(ID)
            train_spec['model_dict'][name] = ID
            train_spec['trained_model_dict'][name] = {}
            for ID_ in self.childrenToList(self.model_tree, ID):
                name_ = self.model_tree.GetItemText(ID)
                train_spec['trained_model_dict'][name][name_] = ID_

        train_spec['checkpoint_name'] = "checkpoint"

        train_spec['solver_list'] = get_optimizer_list()

        return train_spec


        dataset_list = self.childrenToList(self.data_tree, self.data_tree.GetRootItem())
        model_list = self.childrenToList(self.model_tree, self.model_tree.GetRootItem())
        train_spec['dataset_list'] = dataset_list
        train_spec['model_list'] = model_list

        dataset_names = [self.data_tree.GetItemText(x) for x in dataset_list]
        model_names = [self.model_tree.GetItemText(x) for x in model_list]
        train_spec['dataset_names'] = dataset_names
        train_spec['model_names'] = model_names

        trained_model_dict = {}
        trained_model_names_dict = {}
        for model, model_name in zip(model_list, model_names):
            trained_model_list = self.childrenToList(self.model_tree, model)
            trained_model_dict[model_name] = trained_model_list
            trained_model_names_dict[model_name] = [self.model_tree.GetItemText(x) for x in trained_model_list]
        train_spec['trained_model_dict'] = trained_model_dict
        train_spec['trained_model_names_dict'] = trained_model_names_dict
        train_spec['checkpoint_name'] = ''

        train_spec['solver_list'] = get_optimizer_list()

        return train_spec
    
    def getModelsDict(self):
        ### return dict, dict
        ### name:ID, name:dict
        ###         name:ID
        model_dict = {}
        trained_model_dict = {}
        for childID in self.childrenToList(self.model_tree, self.model_tree.GetRootItem()):
            childName = self.model_tree.GetItemText(childID)
            model_dict[childName] = childID
            trained_model_dict[childName] = {}
            for grandchildID in self.childrenToList(self.model_tree, childID):  # dataset
                grandchildName = self.model_tree.GetItemText(grandchildID)
                trained_model_dict[childName][grandchildName] = {}
                for grandgrandchildID in self.childrenToList(self.model_tree, grandchildID): # trained model
                    grandgrandchildName = self.model_tree.GetItemText(grandgrandchildID)
                    trained_model_dict[childName][grandchildName][grandgrandchildName] = grandgrandchildID
        return model_dict, trained_model_dict

    def getDataDict(self):
        ### return dict
        ### name:ID
        dataset_dict = {}
        for ID in self.childrenToList(self.data_tree, self.data_tree.GetRootItem()):
            name = self.data_tree.GetItemText(ID)
            dataset_dict[name] = ID 
        return dataset_dict 

    def getTestSpec(self):
        ### return dict
        ### model_dict, trained_model_dict
        test_spec = {'default_dataset_path':self.data_tree.GetItemData(self.data_tree.GetRootItem())}
        test_spec['model_dict'], test_spec['trained_model_dict'] = self.getModelsDict()
        return test_spec
        
        ### return dict
        ### model_list, model_names, trained_model_list_names
        test_spec['model_dict'] = {}
        test_spec['trained_model_dict'] = {}
        for ID in self.childrenToList(self.model_tree, self.model_tree.GetRootItem()):
            name = self.model_tree.GetItemText(ID)
            test_spec['model_dict'][name] = ID
            test_spec['trained_model_dict'][name] = {}
            for ID_ in self.childrenToList(self.model_tree, ID):
                name_ = self.model_tree.GetItemText(ID)
                test_spec['trained_model_dict'][name][name_] = ID_
        return test_spec

        model_list = self.childrenToList(self.model_tree, self.model_tree.GetRootItem())
        test_spec['model_list'] = model_list
        model_names = [self.model_tree.GetItemText(x) for x in model_list]
        test_spec['model_names'] = model_names

        trained_model_list = []
        trained_model_list_names = []
        for model, model_name in zip(model_list, model_names):
            trained_model_list_ = self.childrenToList(self.model_tree, model)
            trained_model_list_names += [self.model_tree.GetItemText(x) for x in trained_model_list_]
            trained_model_list += trained_model_list_
            #print(model, model_name, trained_model_list_names, trained_model_list)
        test_spec['trained_model_list_names'] = trained_model_list_names
        return test_spec

#    def setTrainSpec(self):
#        pass

    def getDataSpec_(self, dataID):
        res = dict()
        name = self.data_tree.GetItemText(dataID)
        res['name'] = name
        path = self.data_tree.GetItemData(dataID)
        res['path'] = path

        return res

    def getModelSpec_(self, modelID):
        res = dict()
        return res

#    def setTrainSpec_(self):
#        train_spec = {'max_iter': 10000, 'lr':1e-3, 'optimizer':'Adam', 'seed':0, 'batch_size':32, 'checkpoint interval':1000, 'validation interval':1000}
#        train_spec['datasets'] = self.datasets
#        train_spec['models'] = self.models
#
#        train_spec['dataset_names'] = [self.data_tree.GetItemText(x) for x in self.datasets]
#        train_spec['model_names'] = [self.model_tree.GetItemText(x) for x in self.models]
#        return train_spec

#    def getTrainSpec_(self):
#        pass

    def childrenToList(self, tree, item):
        list = []
        child, cookie = tree.GetFirstChild(item)

        while child.IsOk():
            list.append(child)
            child, cookie = tree.GetNextChild(item, cookie)
        return list

    def buildTree(self, tree, rootDir, treeRoot=None):
        #        rootID = tree.AddRoot(os.path.basename(rootDir))
#        tree.SetItemData(rootID, rootDir)
#        self.extendTree(tree, rootID)
#        print(rootID, tree.GetItemData(rootID))

        if treeRoot is None: treeRoot = tree.GetRootItem()

        def itemExist(tree, data, rootID):
            item, cookie = tree.GetFirstChild(rootID)
            while item.IsOk():
                if tree.GetItemData(item) == data:
                    return True
                item, cookie = tree.GetNextChild(rootID, cookie)
            return False

        if tree.IsEmpty() or not itemExist(tree, rootDir, treeRoot):
            rootID = tree.AppendItem(treeRoot, (os.path.basename(rootDir)))
            tree.SetItemData(rootID, rootDir)
            self.extendTree(tree, rootID)
        else:
            print("tree item is already exist!")
        #print(rootID, tree.GetItemData(rootID))

    # input tree, root name, child list
    def appendTree(self, tree, parentID, childlist, model=False):
        for value in childlist:
            if model:
                checkpointdirpath = os.path.join(os.getcwd(), "checkpoint")
                if os.path.exists(checkpointdirpath) and \
                        os.path.exists(os.path.join(checkpointdirpath, value)):
                    trainedmodelpath = os.path.join(checkpointdirpath, value)
                    childID = tree.AppendItem(parentID, value)
                    tree.SetItemData(childID, trainedmodelpath)
                    #tree.SetItemBold(childID, True)
                    self.extendTree(tree, childID)
                else:
                    childID = tree.AppendItem(parentID, value)
                    tree.SetItemData(childID, value)
                    #tree.SetItemBold(childID, True)
            else:
                childID = tree.AppendItem(parentID, value)
                tree.SetItemData(childID, value)
                #tree.SetItemBold(childID, True)
            # print(value, childID, tree.GetItemData(childID))

    def extendTree(self, tree, parentID):
        parentPath = tree.GetItemData(parentID)

        subdirs = os.listdir(parentPath)
        subdirs.sort()
        for child in subdirs:
            childPath = os.path.join(parentPath, child)
            if os.path.isdir(childPath) and not os.path.islink(child) \
                    and not "pycache" in child:
                childID = tree.AppendItem(parentID, child)
                tree.SetItemData(childID, childPath)

                grandsubdirs = os.listdir(childPath)
                grandsubdirs.sort()
                for grandchild in grandsubdirs:
                    grandchildPath = os.path.join(childPath, grandchild)
                    if os.path.isdir(grandchildPath) and not os.path.islink(grandchildPath):
                        grandchildID = tree.AppendItem(childID, grandchild)
                        tree.SetItemData(grandchildID, grandchildPath)



# end of class MyFrame
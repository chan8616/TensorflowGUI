# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.2 on Tue Aug 21 13:46:28 2018
#

import wx
import wx.aui
import os
import sys
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade
from mynotebook import MyNotebook
from utils.util import Redirection

from run import Run

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
        self.buildTree(self.data_tree, self.datasetDir)
        self.data_tree.Expand(self.data_tree.GetRootItem())

        # load model tree (in Modules folder)
        self.modelDir = os.path.join(self.cwd, "checkpoint")
        self.buildTree(self.model_tree, self.modelDir)
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
        print('OnPageChanged')
        if self.notebook.isOnTrainSpec() or self.notebook.isOnTestSpec():
            self.tool_bar.EnableTool(self.tool_run.GetId(), True)
        else:
            self.tool_bar.EnableTool(self.tool_run.GetId(), False)
    def dataTreeOnExpand(self, event):
        itemID = event.GetItem()
        self.data_tree.DeleteChildren(itemID)
        self.extendTree(self.data_tree, itemID)
    def modelTreeOnExpand(self, event):
        itemID = event.GetItem()
        self.model_tree.DeleteChildren(itemID)
        self.extendTree(self.model_tree, itemID)

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
        page = self.notebook.createTestSpecPanel(self.notebook, wx.ID_ANY)
        page.setTestSpec(test_spec)

    def OnTrainSpec(self, event):
        train_spec = self.getTrainSpec()
        page = self.notebook.createTrainSpecPanel(self.notebook, wx.ID_ANY)
        page.setTrainSpec(train_spec)

    def OnRun(self, event):
        page, phase, spec = self.notebook.getRunSpec()
        if spec is not None:
            model_name, trained_model_name, dataset_name = spec['model_name'], spec['trained_model_name'], spec['dataset_name']
            if phase == 'Train':
                if trained_model_name is None:
                    modelID = page.train_spec['model_list'][page.train_spec['model_names'].index(model_name)]
                else:
                    modelID = page.train_spec['trained_model_dict'][model_name]
                datasetID = page.train_spec['dataset_list'][page.train_spec['dataset_names'].index(dataset_name)]
            elif phase == 'Test':
                modelID = page.test_spec['model_list'][page.train_spec['model_names'].index(model_name)]
                datasetID = page.test_spec['dataset_list'][page.test_spec['dataset_names'].index(dataset_name)]

            spec['model_spec'] = self.getModelSpec(modelID)
            """
            return {'type':'None',
                    'n_layer':'None',
                    'input_size':'None',
                    'output_size':'None'}
            """
            spec['dataset_spec'] = self.getDataSpec(datasetID)
            """
            data_spec['name']
            data_spec['path']
            data_spec['label_names']
            data_spec['data']
            data_spec['output_size']
            data_spec['input_types']
            data_spec['input_shapes']
            """

            if phase == 'Train':
                spec_list = [True,
                         spec['model_spec'],
                         spec['dataset_spec'],
                         spec['checkpoint_name'],
                         spec['max_epochs'],
                         spec['batch_size'],
                         spec['optimizer'],
                         spec['learning_rate'],
                         spec['interval'],
                         spec['seed']]
            elif phase == 'Test':
                spec_list = [False,
                         spec['model_spec'],
                         spec['dataset_spec'],
                         spec['interval'],
                         spec['seed']]

            print(**spec_list)
#        self.model_name, self.dataset_name, gpu_selected, \
        #        self.checkpoint, self.epochs, self.batch_size, self.optimizer, \
        #        self.learning_rate, self.interval, self.random_seed \
        #        self.input_shape, self.output_size = spec[1:]

            return Run(spec_list)
        else:
            # self.tool_bar.EnableTool(self.tool_run.GetId(), False)
            pass

    def OnDataSpec(self, item):
        data_spec = self.getDataSpec(item)
        page = self.notebook.createDataSpecPanel(self.notebook, wx.ID_ANY)
        page.setDataSpec(data_spec)

        self.item_to_page[item] = page

    def OnModelSpec(self, item):
        model_spec = self.getModelSpec(item)
        page = self.notebook.createModelSpecPanel(self.notebook, wx.ID_ANY)
        page.setModelSpec(model_spec)

        self.item_to_page[item] = page

    def isDataset(self, item):
        return self.data_tree.GetItemParent(item) == \
                self.data_tree.GetRootItem()

    def treeOnActivated(self, tree, OnSpecFun):
        print('TreeOnActivated')
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
        tree, OnSpecFun = self.model_tree, self.OnModelSpec
        item = tree.GetFocusedItem()

        if tree.GetItemParent(item) == tree.GetRootItem() or \
           tree.GetItemParent(tree.GetItemParent(item)) == tree.GetRootItem():
            if item not in self.item_to_page:
                OnSpecFun(item)
            else:
                _, idx = self.notebook.FindTab(self.item_to_page[item])
                if idx == -1:
                    OnSpecFun(item)
                else:
                    self.notebook.SetSelection(idx)


    def getDataSpec(self, dataID):
        import numpy as np

        data_spec = dict()
        data_name = self.data_tree.GetItemText(dataID)
        data_path = self.data_tree.GetItemData(dataID)
        data_spec['name'] = data_name
        data_spec['path'] = data_path

        childs = os.listdir(data_path)
        # Data/, train.txt, test.txt
        if 'Data' in childs and 'train.txt' in childs and 'test.txt' in childs:
            print('case1')
            path_fun = lambda a: [data_path+'/'+a[0]] + a[1:]
            with open(os.path.join(data_path, 'train.txt'), 'r') as f:
                train = np.array([path_fun(x.split()) for x in f.read().splitlines()])
                x_train = train[:,0]
                y_train = train[:,1]
            with open(os.path.join(data_path, 'test.txt'), 'r') as f:
                test = np.array([path_fun(x.split()) for x in f.read().splitlines()])
                x_test = test[:,0]
                y_test = test[:,1]
            label_names = [str(label) for label in np.unique(y_train.tolist() + y_test.tolist())]
        # train/, test/, labels.txt
        elif 'train' in childs and 'test' in childs and 'labels.txt' in childs:
            print('case2')
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
            train = np.concatenate(([x_train], [y_train]), axis=0).T

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
            test = np.concatenate(([x_test], [y_test]), axis=0).T

        # label/, ... , train.txt, test.txt
        elif 'train.txt' in childs and 'test.txt' in childs:
            print('case3')
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
            train = np.concatenate(([x_train], [y_train]), axis=0).T

            with open(os.path.join(data_path, 'test.txt'), 'r') as f:
                test = f.read().splitlines()
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
            test = np.concatenate(([x_test], [y_test]), axis=0).T

        else:
            print('Invalid Dataset folder %s'%data_path)

        data_spec['label_names'] = label_names
        data_spec['data'] = {'train':train, 'test':test}
        data_spec['output_size'] = str(len(label_names))

        from PIL import Image

        data = np.concatenate((train[:,0], test[:,0]), axis=0)
        types = []
        input_shapes = []
        for x in data:
            fname, ext = os.path.splitext(x)
            if ext not in types:
                types.append(ext)

            if ext == '.png' or ext == '.jpg':
                img = Image.open(x)
                input_shape = img.size
                if input_shape not in input_shapes:
                    input_shapes.append(input_shape)
            else:
                print("We don't support type %s"%ext)

        data_spec['input_types'] = types
        data_spec['input_shapes'] = input_shapes

        return data_spec

    def getModelSpec(self, modelID):
        return {'type':'None',
                'n_layer':'None',
                'input_size':'None',
                'output_size':'None'}
#    def setModelSpec(self):
#        pass

    def getTrainSpec(self):
        train_spec = {'max_epochs': '10000', 'learning_rate':'1e-3', 'optimizer':'Adam', 'seed':'0', 'batch_size':'32', 'interval':'1000'}
        train_spec['lr'] = train_spec['learning_rate']

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
        train_spec['checkpoint_name'] = "datasetname"

        train_spec['gpus'] = ['Not Yet Implemented']

        return train_spec

#    def getTestSpec(self):
#        test_spec = {}
#        test_spec['models'] = self.models
#        test_spec['model_names'] = [self.model_tree.GetItemText(x) for x in self.models]
#        return test_spec

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
            print("Dataset is already exist!")

    def extendTree(self, tree, parentID):
        parentPath = tree.GetItemData(parentID)

        subdirs = os.listdir(parentPath)
        subdirs.sort()
        for child in subdirs:
            childPath = os.path.join(parentPath, child)
            if os.path.isdir(childPath) and not os.path.islink(child):
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

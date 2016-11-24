from DataBox.models import *
from packages.jqgrid import *


class DataSetGrid(JqGrid):
    queryset = DataSet.dataset_objects.all()
    fields = ['id', 'long_name']
    url = "/dataset_grid/"
    # model = DataSet
    colmodel_overrides = {
        'id': {'editable': False, 'width': 6},
        'long_name': {'width': 100},
    }

    # def __init__(self, request):
    #     super(DataSetGrid, self).__init__()
    #     self.queryset = DataSet.dataset_objects.all()


class DictGrid(JqGrid):
    queryset = Dictionary.objects.all()
    fields = ['id', 'name']
    url = "/dict_grid/"
    caption = 'Словники'
    colmodel_overrides = {
        'id': {'editable': False, 'width': 6},
    }


class DictValGrid(JqGrid):
    url = "/dict_val_grid/0"
    fields = ['value']
    caption = 'Значення словника'

    def __init__(self, dict=1):
        super(DictValGrid, self).__init__()
        self.queryset = DictionaryValue.objects.filter(dictionary=dict)


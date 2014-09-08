class MyList:
    def __init___(self):
        self._id2name_map = {}
        self._name2id_map = {}
        
    def add(self, id, name):
        self._name2id_map[name] = id
        self._id2name_map[id] = name
        
    def by_name(self, name):
        id = self._name2id_map[name]
        assert self._id2name_map[id] == name
        return id
        
test = __init__(brandon)
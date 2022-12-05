from skimage.morphology import square, diamond, disk

DILATION_KERNELS = {
    'disk': disk,
    'square': square,
    'diamon': diamond
}

EDGE_WEIGHT = 'weight'

GRAPH_ATTRIBUTER_DEFAULT_PARAMS = {
    'so_feat': {'from_obs': True,
                    'obs_cols': [],
                    'from_X': True,
                    'X_cols': []},
    'deep_feat': {},
    'random_feat': {}
}

OTHER_DEFAULT_PARAMS = {
    'concept_params': 
                {'filter_col':None,
                'labels':None},
    'coordinate_keys': ['x', 'y'],
    'mask_key': 'cellmasks'
}

GRAPH_BUILDER_DEFAULT_PARAMS = {
    'knn': {'builder_params': 
                {'n_neighbors':6, 
                'mode':'connectivity', 
                'metric':'minkowski', 
                'p':2, 
                'metric_params':None, 
                'include_self':True, 
                'n_jobs':-1},
                **OTHER_DEFAULT_PARAMS,
                **GRAPH_ATTRIBUTER_DEFAULT_PARAMS},
    'contact': {'builder_params': 
                    {'dilation_kernel': 'disk',
                     'radius': 4, 
                     'include_self':True},
                **OTHER_DEFAULT_PARAMS,
                **GRAPH_ATTRIBUTER_DEFAULT_PARAMS},
    'radius': {'builder_params': 
                    {'radius': 36, 
                    'mode':'connectivity', 
                    'metric':'minkowski', 
                    'p':2, 
                    'metric_params':None, 
                    'include_self':True, 
                    'n_jobs':-1},
                **OTHER_DEFAULT_PARAMS,
                **GRAPH_ATTRIBUTER_DEFAULT_PARAMS}
}
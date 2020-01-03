from operation.operation_init_func import init_operation

# 初始化 JWTManager
pre_global_init_func = {"operation": [init_operation]}

post_global_init_func = {}
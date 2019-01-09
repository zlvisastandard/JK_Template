class global_var(object):
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    filed_depend = '8'
    data = '9'
    expect = '10'
    result = '11'
def get_id():
    return global_var.Id

def get_url():
    return global_var.url

def get_run():
    return global_var.run

def get_run_way():
    return global_var.request_way

def get_header():
    return global_var.header

def get_data():
    return global_var.data

#获取预期结果col
def get_except():
    return global_var.expect

def get_result():
    return global_var.result

#被依赖的case
def get_case_depend():
    return global_var.case_depend

#被依赖的key
def get_data_depend():
    return global_var.data_depend

#依赖字段
def get_filed_depend():
    return global_var.filed_depend
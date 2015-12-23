from cloudcafe.brm.models.base import BaseBRM


class CreateCustomer(BaseBRM):
    '''
    This is the request class for the Create Customer Flist.
    The request payload is converted from an object to String
    format to aid serialization of request.
    '''
    def __init__(self):
        pass

    def _obj_to_string(self, locale, ip, obj_type1, obj_id, rev_no, flag):
        '''
        This function will return a string to the MAIN class,
        where the string appending to the file.
        '''
        pass

class ObjectRead(BaseBRM):
    '''
    This is the request class for the Object Read Flist.
    The request payload is cob=nverted from an object to string
    format to aid serialization of request.
    '''

    def __init__(self, ip=None, obj_type=None, obj_id=None, rev_no=None):
        self.ip = ip
        self.obj_type = obj_type
        self.obj_id = obj_id
        self.rev_no = rev_no

    def _obj_to_string(self):
        poid = Poid()._obj_to_string(ip = self.ip, obj_type = self.obj_type,
                                     obj_id = self.obj_id,
                                     rev_no = self.rev_no)
        return FileCreate().create_file(poid, "PCM_OP_READ_OBJ")

class PurchaseDeal(BaseBRM):
    '''
    This is the request class for the Purchase Deal Flist.
    The request payload is converted from an object to String
    format to aid serialization of request.
    '''
    def __init__(self, ip=None, obj_type=None, obj_id=None, rev_no=None,
                 obj_id_ser=None, obj_type_ser=None, rev_no_ser=None,
                 cust_center=None, quantity=None, obj_type_pro=None,
                 obj_id_pro=None, rev_no_pro=None, discount=None, status=None,
                 obj_id_pro1=None, obj_type_poid=None, quantity1=None,
                 obj_id_poid=None, rev_no_poid=None, name=None, flag=None):
        self.ip = ip
        self.obj_type = obj_type
        self.obj_type_ser = obj_type_ser
        self.obj_id = obj_id
        self.obj_id_ser = obj_id_ser
        self.rev_no = rev_no
        self.rev_no_ser = rev_no_ser
        self.cust_center = cust_center
        self.quantity = quantity
        self.quantity1 = quantity1
        self.obj_type_pro = obj_type_pro
        self.obj_id_pro = obj_id_pro
        self.rev_no_pro = rev_no_pro
        self.discount = discount
        self.status = status
        self.obj_id_pro1 = obj_id_pro1
        self.obj_type_poid = obj_type_poid
        self.obj_id_poid = obj_id_poid
        self.rev_no_poid = rev_no_poid
        self.name = name
        self.flag = flag
        #print obj_type_poid[0]


    def _obj_to_string(self):
        '''
        This function will return the Flist file for the Purchase Deal.
        '''
        poid = Poid()._obj_to_string(ip = self.ip, obj_type = self.obj_type,
                                     obj_id = self.obj_id,
                                     rev_no = self.rev_no)
        Service_obj = '''0 PIN_FLD_SERVICE_OBJ    ''' + \
        '''POID [0] {ip} {obj_type_ser} {obj_id_ser} {rev_no_ser}'''
        Service_obj = (Service_obj).format(ip = self.ip,
                                           obj_type_ser = self.obj_type_ser,
                                           obj_id_ser = self.obj_id_ser,
                                           rev_no_ser = self.rev_no_ser)
        prgm_name = '''0 PIN_FLD_PROGRAM_NAME    STR [0] "{cust_center}"'''
        prgm_name = (prgm_name).format(cust_center = self.cust_center)
        deal_info = DealInfo()._obj_to_string(quantity = self.quantity,
                                              quantity1 = self.quantity1,
                                              ip = self.ip,
                                              obj_type_pro = self.obj_type_pro,
                                              obj_id_pro = self.obj_id_pro,
                                              rev_no_pro = self.rev_no_pro,
                                              discount = self.discount,
                                              status = self.status,
                                              obj_id_pro1 = self.obj_id_pro1,
                                              obj_type_poid = self.obj_type_poid,
                                              obj_id_poid = self.obj_id_poid,
                                              rev_no_poid = self.rev_no_poid,
                                              name = self.name,
                                              flag = self.flag)
        total_strng = poid +  "\n" + Service_obj + "\n" + prgm_name + "\n" + \
                      deal_info
        return FileCreate().create_file(final_strng = total_strng,
                                        file_name = 'PCM_OP_SUBSCRIPTION_PURCHASE_DEAL')


class Poid(BaseBRM):
    '''
    This is the request class for the Poid.
    The request payload is converted from an object to String
    format to aid serialization of request.
    '''
    def __init__(self, strng=None):
        self.strng = strng


    def _obj_to_string(self, ip, obj_type, obj_id, rev_no):
        '''
        This function will return a string to the CreateCustomer class,
        where the string is appended to the file.
        '''
        strng = '''0 PIN_FLD_POID                      ''' + \
        '''POID [0] {ip} {obj_type} {obj_id} {rev_no}'''
        strng = (strng).format(ip = ip, obj_type = obj_type,
                                obj_id = obj_id, rev_no = rev_no)
        return strng

class DealInfo(BaseBRM):
    '''
    This is the request class for the Deal Info.
    This will return a string to the purchase Deal class.
    '''
    def __init__(self ,strng=None):
        self.strng = strng


    def _obj_to_string(self, quantity, quantity1, ip, obj_type_pro, obj_id_pro,
                       rev_no_pro, discount, status, obj_id_pro1,
                       obj_type_poid, obj_id_poid, rev_no_poid, name, flag):

        strng = '''0 PIN_FLD_DEAL_INFO    SUBSTRUCT [0] allocated 20, used 8
1     PIN_FLD_PRODUCTS      ARRAY [0] allocated 32, used 32
2         PIN_FLD_PURCHASE_END_T TSTAMP [0] (0) <null>
2         PIN_FLD_PURCHASE_START_T TSTAMP [0] (0) <null>
2         PIN_FLD_QUANTITY     DECIMAL [0] {quantity}
2         PIN_FLD_PRODUCT_OBJ    POID [0] {ip} {obj_type_pro} {obj_id_pro} {rev_no_pro}
2         PIN_FLD_USAGE_DISCOUNT DECIMAL [0] {discount}
2         PIN_FLD_CYCLE_DISCOUNT DECIMAL [0] {discount}
2         PIN_FLD_PURCHASE_DISCOUNT DECIMAL [0] {discount}
2         PIN_FLD_STATUS         ENUM [0] {status}
2         PIN_FLD_USAGE_END_T  TSTAMP [0] (0) <null>
2         PIN_FLD_USAGE_START_T TSTAMP [0] (0) <null>
2         PIN_FLD_CYCLE_END_T  TSTAMP [0] (0) <null>
2         PIN_FLD_CYCLE_START_T TSTAMP [0] (0) <null>
1     PIN_FLD_PRODUCTS      ARRAY [1] allocated 32, used 32
2         PIN_FLD_PURCHASE_END_T TSTAMP [0] (0) <null>
2         PIN_FLD_PURCHASE_START_T TSTAMP [0] (0) <null>
2         PIN_FLD_QUANTITY     DECIMAL [0] {quantity1}
2         PIN_FLD_PRODUCT_OBJ    POID [0] {ip} {obj_type_pro} {obj_id_pro1} {rev_no_pro}
2         PIN_FLD_USAGE_DISCOUNT DECIMAL [0] {discount}
2         PIN_FLD_CYCLE_DISCOUNT DECIMAL [0] {discount}
2         PIN_FLD_PURCHASE_DISCOUNT DECIMAL [0] {discount}
2         PIN_FLD_STATUS         ENUM [0] {status}
2         PIN_FLD_USAGE_END_T  TSTAMP [0] (0) <null>
2         PIN_FLD_USAGE_START_T TSTAMP [0] (0) <null>
2         PIN_FLD_CYCLE_END_T  TSTAMP [0] (0) <null>
2         PIN_FLD_CYCLE_START_T TSTAMP [0] (0) <null>
1     PIN_FLD_NAME            STR [0] "{name}"
1     PIN_FLD_POID           POID [0] {ip} {obj_type_poid} {obj_id_poid} {rev_no_poid}
1     PIN_FLD_END_T        TSTAMP [0] (0) <null>
1     PIN_FLD_FLAGS           INT [0] {flag}
1     PIN_FLD_START_T      TSTAMP [0] (0) <null>
1     PIN_FLD_DESCR           STR [0] "{name}"'''
        strng = (strng).format(quantity = quantity, ip = ip, quantity1 = quantity1,
                 obj_type_pro = obj_type_pro, obj_id_pro = obj_id_pro,
                 rev_no_pro = rev_no_pro, discount = discount,
                 status = status, obj_id_pro1 = obj_id_pro1,
                 obj_type_poid = obj_type_poid, obj_id_poid = obj_id_poid,
                 rev_no_poid = rev_no_poid, name = name, flag = flag)

        return strng

class FileCreate(BaseBRM):
    '''
    This class is used to create a file with the give string.
    It will take two parameters, 1. String to place in file,
    2. File Name with full path.
    '''
    def __init__(self, final_strng=None, file_name=None):
        self.final_strng = final_strng
        self.file_name = file_name

    def create_file(self, final_strng, file_name):
        file_data = open(file_name, 'w')
        file_data.write(final_strng)
        file_data.close()



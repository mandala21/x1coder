import unittest

class TestJsonStruct(unittest.TestCase):
    def assertJsonStruct(self, data, struct):
        """
        Check if input contains all struct data
        ex:
        input:
        {
            "user": "Lucas Resende",
            "email": "blabla@email.com"
        }
        struct:
        {
            "user": str
        }
        OK
        -------------------------------------------
        input:
        {
            "user": "Lucas Resende",
            "email": "blabla@emai.com"
        }
        struct:
        {
            "user": str,
            "phone": str,
        }
        FALID
        """
        #interation in all keys of input and check if in struct
        for key in data.keys():
            if key in struct:
                if isinstance(data[key],struct[key]):
                    struct.pop(key)
        #if len of struct is zero then all in struct in input
        if len(struct) != 0:
            keys_falied = ""
            for failed in struct.keys():
                keys_falied += failed + ' '
            raise AssertionError('Keys not found: ' + keys_falied)
        
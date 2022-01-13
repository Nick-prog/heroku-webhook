import Webhook
import sys
import ctypes

try:
    total1 = Webhook.total(method=1)
    Webhook.uploaded_documents()
    ctypes.windll.user32.MessageBoxW(0, "%s uploaded documents pulled." %(total1), "Complete!", 64)

    total2 = Webhook.total(method=2)
    Webhook.fee_documents()
    ctypes.windll.user32.MessageBoxW(0, "%s fee documents pulled." %(total2), "Complete!", 64)
except ValueError:
    ctypes.windll.user32.MessageBoxW(0, "ValueError encountered at entry %s. %s" %(len(Webhook.IDs), sys.exc_info()[1]), "Warning!", 16)
    pass
except TypeError:
    ctypes.windll.user32.MessageBoxW(0, "TypeError encountered at entry %s. %s" %(len(Webhook.IDs), sys.exc_info()[1]), "Warning!", 16)
    pass
except:
    ctypes.windll.user32.MessageBoxW(0, "Something terrible occurred at entry %s. %s, %s" %(len(Webhook.IDs), sys.exc_info()[0], sys.exc_info()[1]), "Warning!", 16)
    pass

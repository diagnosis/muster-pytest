import muster_pytest.models
from muster_pytest.models import Outing, Hiker
from muster_pytest import models as m

print(f"running {__name__}")

a = Outing("Rainer", 2)
h = m.Hiker("Safa")
print(a, h)
print(Outing is m.Outing)

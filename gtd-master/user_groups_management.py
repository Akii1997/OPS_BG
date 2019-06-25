import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.contrib.auth.models import User, Group
import sheet_google_activation as sp
import pandas as pd

x = sp.get_df('1_fsNwvmdUQH0IswmWtGdHtjBU-N2eT9RqLEVeUXczdA', 'Sheet1')
df = pd.DataFrame(x[1:], columns=x[0])
df = df.iloc[:5, 0:3]
for row in df.itertuples(index=True, name='Pandas'):
    user, created = User.objects.get_or_create(username=getattr(row, "email"),
                                      email=getattr(row, "email"), password=getattr(row, "number"),
                                               first_name=getattr(row, "name"), is_staff=False)
    if created:
        my_group = Group.objects.get(name='OPS_BG_Task')
        my_group.user_set.add(user)
    else:
        pass
gm = User.objects.filter(is_staff=False)
for name in gm:
    if name.get_short_name() in df.name.values:
        pass
    else:
        name.delete()


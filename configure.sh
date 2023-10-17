sudo sed -i "s/RHT_COURSE=.*/RHT_COURSE=bfx010/" /etc/rht
sudo sed -i "s/RHT_VERSION_LOCK=.*/RHT_VERSION_LOCK='>=7.0,<8.0'/" /etc/rht
sudo systemctl restart dynolabs-update.service
pip install rht-labs-bfx010==7.0.1.dev7 --extra-index-url https://pypi.apps.tools-na.prod.nextcle.com/repository/labs/simple/
lab select bfx010
lab --version
source ~/.venv/labs/bin/activate
cd .venv/labs/lib/python3.6/site-packages/bfx010/
# git clone https://YogiSoni-lazy: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@github.com/YogiSoni-lazy/bfx010.git
# lab start breakfix010-maintainenceLVM
# lab grade breakfix010-maintainenceLVM
# lab finish breakfix010-maintainenceLVM

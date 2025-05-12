
# X7-Deauth Tool
## Instagram: @amen_labidi

X7-Deauth Tool هو أداة قوية لتنفيذ هجمات **Deauthentication** على الشبكات اللاسلكية (Wi-Fi). تستخدم الأداة تقنية **Wi-Fi Deauth Attack** لقطع الاتصال بين جهاز العميل (مثل الهاتف أو الكمبيوتر) والنقطة اللاسلكية (Access Point).

## المتطلبات
قبل أن تبدأ، تأكد من أن لديك الأدوات التالية على جهازك:

- **Kali Linux** أو أي توزيعة تدعم Wi-Fi monitor mode مثل **Parrot OS**.
- **aircrack-ng**: لتفعيل وضع المراقبة (Monitor Mode).
- **Scapy**: مكتبة Python لتوليد وإرسال الحزم.
- **Python 3**: لتشغيل السكربت.

### تثبيت الأدوات
لتثبيت الأدوات المطلوبة، يمكنك تنفيذ الأوامر التالية على Kali Linux أو توزيعة مشابهة:

```bash
# تثبيت Scapy
sudo apt update
sudo apt install python3-scapy

# تثبيت aircrack-ng
sudo apt install aircrack-ng
```

## الإعداد

1. تأكد من أن لديك جهاز واي فاي يدعم **Monitor Mode** و **Packet Injection**. يمكنك التحقق باستخدام:

   ```bash
   iwconfig
   ```

2. قم بتفعيل **Monitor Mode** على واجهتك اللاسلكية:

   ```bash
   sudo airmon-ng start wlan0
   ```

   يجب أن تتحول واجهتك إلى `wlan0mon`.

3. تأكد من أن واجهتك في **Monitor Mode** عبر:

   ```bash
   iwconfig
   ```

4. قم بتشغيل الأداة من خلال السكربت المناسب:

   - **لنسخة CLI** (Command Line Interface):
     ```bash
     sudo python3 cli/x7_deauth.py
     ```

   - **لنسخة GUI** (Graphical User Interface):
     ```bash
     sudo python3 gui/x7_deauth_gui.py
     ```

## كيفية الاستخدام

1. بعد تشغيل السكربت، سيتم مسح الشبكات المتاحة وعرضها في قائمة.
2. اختر الشبكة التي تريد تنفيذ هجوم **Deauthentication** عليها.
3. الأداة ستبدأ بإرسال حزم deauth لقطع الاتصال بين العميل والنقطة اللاسلكية.
4. إذا كنت تستخدم النسخة **GUI**، يمكنك التفاعل مع الأداة عبر واجهة رسومية تحتوي على زر لبدء الهجوم ووقفه.
5. لتوقف الهجوم، يمكنك استخدام الأمر:

   ```bash
   sudo pkill airodump-ng
   ```

## ملاحظات
- **المسؤولية**: هذه الأداة يجب أن تستخدم فقط في البيئات التجريبية والمشروعة (مثلاً لاختبار الأمان على شبكتك الشخصية).
- **القوانين**: تأكد من أنك تعرف القوانين المحلية المتعلقة باستخدام هذه الأدوات قبل استخدامها.

## المساهمة

إذا كنت ترغب في المساهمة في تحسين الأداة، يمكنك رفع طلبات السحب (Pull Requests) أو فتح مشاكل (Issues) على GitHub.

## الاتصال

لأي استفسارات أو دعم، يمكنك التواصل مع صاحب الأداة عبر **Instagram**: [@amen_labidi](https://www.instagram.com/amen_labidi/).

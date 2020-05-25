from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
    today=date.today()
    print("today's date::"+str(today))

    print("day components::", today.day, today.month, today.year)

    print("Today's weekday::", today.weekday())
    days=["mon", "tue", "wed", "thurs", "fri"]
    print("today's weekday is::" , days[today.weekday()])

    today=datetime.now()
    print(today)
    t=datetime.time(datetime.now())
    print(t)

    print(timedelta(days=365, hours=5, minutes=1))
    now=datetime.now()
    print("today is::"+str(now))
    print("one year from now will be::"+str(now+timedelta(days=365)))
    print("2 days and 3 weeks from now will be::"+str(now+timedelta(days=2, weeks=3)))
 
    #formatted string uding strftime
    #%Y/%y year
    #%a/%Y weekday
    #%b/%B month
    #%d day of month
    #%c locale datetime
    #%x locale date
    #%X locale time
    #%I/%H 12/24 hour
    #%M minutes
    #%S seconds
    #%p am/pm
    print("current year is::"+datetime.now().strftime("%Y"))
    #calculate date one week age string formatted
    t=datetime.now()-timedelta(weeks=1)
    s=t.strftime("%A %B %d, %Y")
    print("1 week back from now was::"+s)

    today=date.today()
    tom=today+timedelta(days=1)
    print("tomorrow::"+str(tom))


main()
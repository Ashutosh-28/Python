def convert_seconds(seconds):
    hours=seconds//3600  #prints integer part of division
    minutes= (seconds-hours*3600)//60
    remaining_seconds= seconds- hours*3600-minutes*60
    return hours,minutes,remaining_seconds

hours,minutes,seconds= convert_seconds(9000)
print(hours,minutes,seconds)

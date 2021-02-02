time_for_pic = int(input())
scenes = int(input())
one_scene_duration = int(input())

preparation = time_for_pic * 0.15
time_for_scenes = scenes * one_scene_duration
time_needed = preparation + time_for_scenes
time_not_enougt = time_needed - time_for_pic
if time_needed <= time_for_pic:
    print(f"You managed to finish the movie on time! You have {abs(time_not_enougt):.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {time_not_enougt:.0f} minutes.")
mondayClass ={"alice","bob","charlie","diana"}
wednesdayClass ={"bob", "diana", "eve", "frank"}

mondayClass.add("Grace")
print("monday class", mondayClass)
print("wednesday class", wednesdayClass)
bothclasses =mondayClass &  wednesdayClass
print("attended both class:", bothclasses)
allStudents = mondayClass | wednesdayClass
print("attended either classes:", allStudents)
onlyOne = mondayClass ^ wednesdayClass
print("only one class:", onlyOne)
print("is monday subset of all student?", mondayClass <= allStudents)
'''
১। student_name = [] একটি খালি লিস্ট নেই এবং কিছু স্টুডেন্টের নাম যোগ করি 
২। marks = [] একটি খালি লিস্ট নেই তার মধ্যে স্টুডেন্টের মার্ক নেই। 
৩। has_passed = [] একটি খালি লিস্ট নেই এবং যে সকল স্টুডেন্টের 
মার্ক ৪০ এর উপড়ে তাদেরক True  এবং যাদের মার্ক ৪০ এর নিছে তাদেরকে False দেই।
৪। স্টুডেন্টের নাম মার্ক এবং পাশ ফেল প্রিন্ট কর। 
'''
student_name = []
student_name.append('rakib')
student_name.append('sakib')
student_name.append('tamim')

marks = []
marks.append(50)
marks.append(60)
marks.append(35)

has_passed = []

for mark in marks:
    if mark < 40:
        has_passed.append(False)
    else:
        has_passed.append(True)
print("Student name -- mark --Result")
for student, mark, result in zip(student_name,marks, has_passed):
    print(f"{student} -- {mark} --{result}")

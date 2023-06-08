---
layout: page
title: Policies
nav_order: 2
description: >-
    Course policies and information.
---

# Policies
{:.no_toc}

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---
Please note: Course policies are subject to change.

## About the Course

This course is an introduction to the field of robotics. It covers the fundamentals of kinematics, dynamics, and control of robot manipulators, robotic vision, and sensing. The course deals with forward and inverse kinematics of serial chain manipulators, the manipulator Jacobian, force relations, dynamics, and control. It presents elementary principles on computer vision and robot motion planning. The course concludes with current applications of robotics in active perception, medical robotics, autonomous vehicles, and other areas. **Students are expected to have a background in linear algebra, calculus, and basic physics, as well as familiarity with the Python programming language.** The lectures are supplemented with homeworks and experimental work in the laboratory using simulations based on several <a href="http://www.rethinkrobotics.com/baxter/">Baxter</a>, <a href="http://www.rethinkrobotics.com/sawyer/">Sawyer</a>, and <a href="http://www.turtlebot.com/turtlebot2/">TurtleBot</a> robots. There are two midterms, but no final exam. The last month of the course is devoted to the design and implementation of a final project, carried out individually or in groups of approximately four students.

Questions regarding homeworks, exams, lectures, and discussions should be directed to a Discussion TA. Questions regarding labs should be directed to a Lab TA. Questions regarding course logistics should be directed to Riddhi. You can check the Staff page to see who can best respond to your question. All questions can and should be directed to Edstem for the fastest response. When emailing a GSI, please prefix the subject line with [EECS C106A].

**Note all following dates and times are in PST/PDT.**

## Resources

The required text is Richard Murray, Zexiang Li and S. Shankar Sastry’s *A Mathematical Introduction to Robotic Manipulation* (first edition digitally available <a href="http://www.cds.caltech.edu/~murray/mlswiki/?title=First_edition">here</a>). The errata which contain the known errors can be found at <a href = "https://www.cds.caltech.edu/~murray/books/MLS/index.html">this link</a>. Additional lectures will cover the basics of computer vision, path planning, state estimation, and control. We will also use supplementary material from
the book by Ma Yi, Stefano Soatto, Jana Kosecka, and Shankar Sastry *An Invitation to 3 D Vision: From Images to Geometric Models*, Springer Verlag, 2004 (slides willl be provided) and from the motion planning book of Howie Choset, Kevin Lynch, Seth Hutchinson, George Kantor, Wolfram Burgard, and Sebastian Thrun *Principles of Robot Motion Planning: Theory, Algorithms, and Implementation*, MIT Press, 2005. You are not required to purchase these two references.

## Disability Accommodations & Emergencies

If you need disability-related accommodations in this class, if you have emergency medical information you wish to share with us, or if you need special arrangements in case the building must be evacuated, please inform us immediately. Please see the professor or GSIs privately after class or send us an email.

## Grade Breakdown

|Homeworks| 20%|
|Midterms| 20%|
|Labs| 20%|
|Final Project| 40%|

## Lectures

Lecture attendance is not mandatory, but we highly recommend attending live lecture if possible. Lectures will be held synchronously on Tuesdays and Thursdays, 11:00 am - 12:30 pm. Lectures will be recorded and posted for students who cannot attend live lecture.

Lectures will be composed of 2-3 "modules", with quick discussion and question breaks in between. You will have the opportunity to ask clarifying questions and have the professor or a TA respond in real time.

## Homeworks

Homeworks will be collected and graded using the Gradescope system. Create an account on gradescope.com with your Berkeley email account and SID. Add this course with the code **57KNVR**.

There will be a total of 10 homeworks, due weekly through mid-November (with the exception of midterm weeks). Homework will be released in the evening each Wednesday, starting August 25 (the first day of class). You will have until 11:59pm the following Tuesday to complete each assignment.

|**Assignment**|**Assigned @5pm**|**Due @11:59pm**|
| HW 0 | 08/25 | 08/30 |
| HW 1 | 08/31 | 09/06 |
| HW 2 | 09/07 | 09/13 |
| HW 3 | 09/14 | 09/20 |
| HW 4 | 09/21 | 09/27 |
| HW 5 | 10/05 | 10/11 |
| HW 6 | 10/12 | 10/18 |
| HW 7 | 10/19 | 10/25 |
| HW 8 | 10/26 | 11/01 |
| HW 9 | 11/02 | 11/08 |

Each student is allocated 5 total days of extension (also known as *slip days*), to be used on any homework assignment with no loss of points. To allow for homework solutions to be released in a timely manner, **no more than 2 extension days may be used on a single assignment.** After using all extension days, homeworks will not receive credit. Note: Homework will not be accepted more than two days past the due date, barring extenuating circumstances.

Collaboration on homework sets is encouraged, but all students must write up their own solution set. Additionally, every student is accountable for the solutions they submit and may be asked to discuss them with a GSI or instructor. **Please list all collaborators at the top of each submitted homework set.**

We will hold **weekly homework parties!** They will be held each Monday 6:00pm - 8:00pm. They will be staffed by TAs and readers to assist students working through the homework. These hours are dedicated to homework only.

Additionally, you will receive one homework drop if you complete both post-midterm surveys.

## Midterms

There will be two midterms covering the course material, on **Thursday, September 29**, and **Tuesday, November 15**. The midterms will be held in person during class time.
Students will be allowed a cheat sheet.

## Labs

Labs must be done in person to receive full credit. Students will be working with hardware in the labs.

Lab sections will meet each week beginning the first full week of classes (starting 8/29) and will run through the week of November 12. We will do our best to assign you to a lab section that you are regularly able to attend, as we rely on an even distribution of students for fair access to support from course staff. You will complete each lab with one partner; no groups of three will be allowed. In lieu of formal reports, labs are completed by discussing your system with and demonstrating its functionality to your lab GSI during various “check-offs” specified in each lab description. **Note that all students who are being checked off must be present at the time of the check-off, in the interest of making sure everyone can fully explain the code and system functionality.** 

Labs may be worked on outside of class hours. Additionally, labs may be checked off at the office hours of any Lab TA, or you may request to attend a different lab section for the check-off by asking a GSI. Note that many of the labs in this class are full, and you will not be allowed to attend them.

Labs should ideally be completed by the end of your assigned lab section, and are scoped such that this should be feasible. We recognize, however, that due to different levels of previous experience with the material this will not always be possible. In order to accommodate this variation while ensuring that students do not fall behind, we have developed the following (admittedly complex) policies:

- Labs 1-2 are a serial introduction to ROS and the other tools used in this class. They must therefore be completed by the *start* of your assigned lab section the following week.
- Labs 3-8 occur in Modules of two labs each (3 & 4, 5 & 6, 7 & 8); each Module is dependent on the previous Module, but labs within each Module are not dependent on each other. Modules are 3 weeks long. At the start of the first week of a Module, the odd-numbered lab will be released. At the start of the second week of the Module, the even-numbered lab will be released. The third and final week of the Module is a buffer week, intended to be used if you were unable to complete the lab(s) during this module. You will receive full credit for any check-offs during the buffer week for any labs in the current module. Both labs from the module are due at the start of your lab section the week after your buffer week (ie: the start of the lab when you begin a new Module).
- Week 3 of Module 3 will also be used to provide final project feedback

*The start of your lab section is a hard cutoff — that is, if an assignment is due at the start of lab section, you may **not** check off that assignment at the start of class for full credit; it must be checked off beforehand. This policy is in place because many of the labs fully fill the allotted time, and we want to keep everyone on schedule.* If you miss the checkoff deadline for a lab, you will have one week after the due date to receive 50% credit.


|**Lab**|**Assigned**|**Due Week Of**|
| Lab 1 | 08/28 | 09/04 |
| Lab 2 | 09/04 | 09/11 |
| Lab 3 | 09/11 | 10/02 |
| Lab 4 | 09/11 | 10/02 |
| Lab 5 | 10/02 | 10/23 |
| Lab 6 | 10/02 | 10/23 |
| Lab 7 | 10/23 | 11/13 |
| Lab 8 | 10/23 | 11/13 |


We understand that these policies are a bit nuanced,  and if you have questions,  please ask us!  We’ve done our best to create a policy that allows for flexibility while encouraging people to stay on schedule and maintaining fairness; to do so, we’ve sacrificed simplicity.

**Please do not make your lab respositories public, even after you finish the course. We're doing our best to uphold academic honesty!**

## Discussions
Discussion sections will be held on Thursday 2:00pm - 3:00pm (Cory 400), Friday 2:00pm - 3:00pm (Cory 521), and Friday 3:00pm - 4:00pm (Cory 521). Attendance is recommended, but not mandatory.

Friday sections are held in person in Cory 521.
The Thursday 2-3pm section will be held in person in Cory 400 and recorded. Because discussion section is recorded, please note that if you ask a question, you will be recorded as well. If privacy is a concern, please consider turning off your camera before speaking.

## Lost and Overwhelmed Students’ Turnabout (LOST) Section

We will be hosting LOST Section on Wednesdays 5:00pm - 7:00pm, location forthcoming. This section is dedicated to providing a safe space for students who feel as though they are lost or falling behind in the course. The LOST section will lag one week behind the lecture pace so students have time to formulate questions and ask them. Each week, a poll will be released to ask students what topics they would like to be covered in a “mini-lecture” at the start of LOST section. After the mini-lecture, students will have the opportunity to work on additional problems and ask more questions.

This section is NOT intended to be used as a review session.


## Final Project

The final project will constitute the largest single portion of your grade for this course and must include sensing, planning, and actuation components on real hardware. Project deliverables include a proposal, a video, a live demo, a final report, and several intermediate check-ins. Further information will be forthcoming. Due to the types of deliverables involved (e.g., live demonstrations), extension days may not be used on project deliverables, and late work will not be accepted.

All students must complete a final project. Failure to complete a final project will result in a failing grade.

## Office Hours

The instructors will hold weekly office hours to discuss lecture content, homework assignments, projects, and other course material. We will try our best to schedule them so that each student has the opportunity to attend at least one office hour each week. When discussing a current homework assignment, instructors will **not** provide solutions. Rather, instructors will be happy to help clarify fundamentals and to guide students’ reasoning in related problems.

If you are unable to attend office hours, please utilize the Edstem for this class. We cannot guar     antee response time from instructors, but we highly recommend helping your classmates out as you can! 

Please take all homework, discussion, and lecture questions to Discussion TAs. All lab questions should be discussed with Lab TAs. Any administrative questions should be directed to Riddhi. If you do not follow these guidelines, there are no guarantees your questions will be answered.

## A Note on Late Work

While  we  will  abide  by  the  policies  listed  above  regarding  specific  assignment  types,  we  understand  that unforeseen circumstances do happen.  If you feel that you will not be able to complete an assignment on time under the policies listed above due to truly extenuating circumstances, please inform a course instructor as soon as possible and before the associated deadline to discuss your situation. Once the deadline has passed, accommodations are unlikely.

## Regrade Requests

If you feel that your work has been graded unfairly, you may request a regrade by submitting a request on Gradescope with a written statement explaining the mistake. Be aware that points may be deducted as well as added if a regrade is requested.

<!-- ## Due Dates

Here are some of the key assignments this semester (organized by due date). Lab due dates can be found in the Lab section of this document.

|**Assignment**|**Assigned**|**Due**|
| HW 0 | 08/26 5pm | 09/01 11:59pm |
| HW 1 | 09/02 5pm | 09/08 11:59pm |
| HW 2 | 09/09 5pm | 09/15 11:59pm |
| HW 3 | 09/16 5pm | 09/22 11:59pm |
| HW 4 | 09/23 5pm | 09/29 11:59pm |
| **Midterm I** | 09/30 8pm | 10/01 8pm |
| **Final Project Mini-Proposal & Team** | 10/02 Discussion | 10/09 11:59pm |
| HW 5 | 10/07 5pm | 10/13 11:59pm |
| HW 6 | 10/14 5pm | 10/20 11:59pm |
| HW 7 | 10/21 5pm | 10/27 11:59pm |
| **Final Project Proposal & Parts List** | week of 10/19 | 10/30 11:59pm |
| HW 8 | 10/28 5pm | 11/03 11:59pm |
| HW 9 | 11/04 5pm | 11/10 11:59pm |
| **Midterm II** | 11/18 8pm | 11/19 8pm |
| **Final Project Presentations** | Assignments TBD | 12/10 & 12/11 |
| **Final Project Reports** | 10/30 | 12/18 11:59pm | -->

## Advice 

The following tips are offered based on our experience.

**Do the homeworks!** The homeworks are explicitly designed to help you to learn the material as you go along. Although the numerical weight of the homeworks is not huge, there is usually a strong correlation between homework scores and final grades in the class.

**Keep up with lectures!** Discussion sections, labs and homeworks all touch on portions of what we discuss in lecture. Students do much better if they stay on track with the course. That will also help you keep the pace with your homework and study group.

**Take part in discussion sections!** Discussion sections are not auxiliary lectures. They are an opportunity for interactive learning. The success of a discussion section depends largely on the willingness of students to participate actively in it. As with office hours, the better prepared you are for the discussion, the more you are likely to benefit from it.

**Come to office hours and homework party!** We love to talk to you and do a deep dive to help you understand the material better.

**Form study groups!** As stated above, you are encouraged to form small groups (two to four people) to work together on homeworks and on understanding the class material on a regular basis. In addition to being fun, this can save you a lot of time by generating ideas quickly and preventing you from getting hung up on some point or other. Of course, it is your responsibility to ensure that you contribute actively to the group; passive listening will likely not help you much. Also recall the caveat above, that you must write up your solutions on your own. We strongly advise you to spend some time on your own thinking about each problem before you meet with your study partners; this way, you will be in a position to compare ideas with your partners, and it will get you in practice for the exams. Make sure you work through all problems yourself, and that your final write-up is your own. Some groups try to split up the problems ("you do Problem 1, I'll do Problem 2, then we'll swap notes"); not only is this a punishable violation of our collaboration policies, it also ensures you will learn a lot less from this course.

We understand that there is a lot happening and this semester will have its unique challenges. We are here to support you throughout the semester, both as students *and as people.* Life happens, and we want to make sure you are still receiving a quality education despite the current state of the world. **Please communicate with us** if you are experiencing extenuating circumstances and need extra support. We're here for you.
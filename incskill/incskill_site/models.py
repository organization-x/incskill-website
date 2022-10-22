import random
from django.db import models
from django.contrib.auth.models import User
from django_postgres_extensions.models.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Question(models.Model):
    all_questions = []
    query = models.CharField(max_length=1000)
    corr_ans = models.CharField(max_length=1000)
    inc_ans1 = models.CharField(max_length=1000)
    inc_ans2 = models.CharField(max_length=1000)
    inc_ans3 = models.CharField(max_length=1000)
    answers = ['', '', '', '']
    def __init__(self, query, corr_ans, inc_ans1, inc_ans2, inc_ans3):
        self.query = query
        self.corr_ans = corr_ans
        self.inc_ans1 = inc_ans1
        self.inc_ans2 = inc_ans2
        self.inc_ans3 = inc_ans3
        Question.all_questions.append(self)
    

    def randomize(self):
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
        while(rand2 == rand1):
            rand2 = random.randint(0,3)
        rand3 = random.randint(0,3) 
        while(rand3 == rand1 and rand3 == rand2):
            rand3 = random.randint(0, 3)
        rand4 = random.randint(0,3) 
        while(rand4 == rand1 and rand4 == rand2 and rand4 == rand3):
            rand4 = random.randint(0, 3)
        self.answers[rand1] = self.inc_ans1
        self.answers[rand2] = self.inc_ans2
        self.answers[rand3] = self.inc_ans3
        self.answers[rand4] = self.corr_ans

    def check_ans(self, selected_ans):
        if self.corr_ans == selected_ans:
            return True
        else:
            return False 

class Quiz:
    questions = []
    potential_score = 0
    all_quizes = []

    def __init__(self) :
        Quiz.all_quizes.append(self)
    
    def add_question(self, question:Question):
        self.questions.append(question)
        self.potential_score += 1
    
    def del_question(self, index):
        if (index < len(self.questions)):
            print("Deletion successful")
            del self.questions[index]
        else: 
            print("Deletion unsuccessful, index out of bounds")

    def start_quiz(self, instance:User):
        instance.profile.quiz_score = 0
        instance.profile.curr_quiz_index = 0
        instance.curr_question = self.questions[0]

    def submit_answer(self, instance:User, submitted_ans):
        if (instance.profile.curr_question.check_ans(submitted_ans)):
            instance.profile.quiz_score += 1
            save_user_profile(sender=User, instance=instance)
        if (instance.profile.curr_quiz_index < len(self.questions) - 1):
            instance.profile.curr_quiz_index += 1
            instance.profile.curr_question = self.questions[instance.profile.curr_quiz_index]
            return True
        else:

            return False

def get_default_question():
        return Question.objects.get_or_create(
            query='default', corr_ans='default', inc_ans1='default', inc_ans2='default', inc_ans3='default')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    progress = models.FloatField(default = 0.0)
    resource1 = models.BooleanField(default=False)
    resource2 = models.BooleanField(default=False)
    resource3 = models.BooleanField(default=False)
    resource4 = models.BooleanField(default=False)
    resource5 = models.BooleanField(default=False)
    resource6 = models.BooleanField(default=False)
    resource7 = models.BooleanField(default=False)
    resource8 = models.BooleanField(default=False)
    resource9 = models.BooleanField(default=False)
    resource10 = models.BooleanField(default=False)
    resource11 = models.BooleanField(default=False)
    resource12 = models.BooleanField(default=False)
    quiz_complete = ArrayField(base_field=models.BooleanField(default=False), blank=True, null=True)
    quiz_score = models.IntegerField(default = 0)
    curr_quiz_index = models.IntegerField(default = 0)
    curr_question = models.ForeignKey("Question", null=True, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def calculate_progress(sender, instance, **kwargs):
    progress = instance.profile.progress = 0.0
    if instance.profile.resource1:
        progress += (100/14)
    if instance.profile.resource2:
        progress += (100/14)   
    if instance.profile.resource3:
        progress += (100/14)
    if instance.profile.resource4:
        progress += (100/14)
    if instance.profile.resource5:
        progress += (100/14)
    if instance.profile.resource6:
        progress += (100/14)
    if instance.profile.resource7:
        progress += (100/14) 
    if instance.profile.resource8:
        progress += (100/14)
    if instance.profile.resource9:
        progress += (100/14)
    if instance.profile.resource10:
        progress += (100/14)   
    if instance.profile.resource11:
        progress += (100/14)
    if instance.profile.resource12:
        progress += (100/14)

    
    instance.profile.progress = round(progress, 2)
    save_user_profile(sender=User, instance=instance)


        


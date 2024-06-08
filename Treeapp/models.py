from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name



# class Role(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name      
    
# class User(models.Model):
#     first_name=models.CharField(max_length=250)
#     last_name=models.CharField(max_length=250)
#     email=models.EmailField(unique=True ,null=False)
#     password=models.CharField(max_length=250)
#     role_id=models.OneToOneField(Role, on_delete=models.DO_NOTHING)
    
    
#     def __str__(self):
#         return self.first_name    
    
    
    

        
    
# class requestor(models.Model):
#     user_id= user_id=models.OneToOneField(User, on_delete=models.DO_NOTHING)
    
    
#     class admin(models.Model):
#         user_id=models.OneToOneField(User, on_delete=models.DO_NOTHING)
#         phone_no=models.IntegerField()
#         # def __str__(self):
#         #     return self.name    

  
    
# class orginization(models.Model):
#    email=models.EmailField(unique=True ,null=False)
#    password=models.CharField(max_length=250)
#    established_date=models.DateField()
#    requestor_id=models.OneToOneField(requestor, on_delete=models.DO_NOTHING)
   
#    def __str__(self):
#             return self.email 
   
   
   
# class quotation(models.Model):
#     requestor_id=models.OneToOneField(requestor, on_delete=models.DO_NOTHING)
#     date_created=models.DateField()
#     status=models.BooleanField(default=False,null=True,blank=False)
    
    
# class alloy(models.Model):
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

#     name=models.CharField(max_length=250)  
    
    
#     class MPTTMeta:
#         order_insertion_by = ['name']

#     def __str__(self):
#         return self.name  
    
       
# class  quotationDetail(models.Model):
#     test_id=models.IntegerField()
#     test_condition_id=models.IntegerField()      
#     quotation_id=models.IntegerField()       
#     alloy_id=models.OneToOneField(alloy, on_delete=models.DO_NOTHING)      
#     object_quantity=models.IntegerField()       
#     test_condition_value=models.IntegerField()       
#     unit_id=models.IntegerField()       
#     test_object_id=models.IntegerField()   
    
    
    
# class quotationTestParameter(models.Model):
#          test_parameter_id=models.   
#          quotetion_details_id=models.   
#          test_parametor_value=models.
#          unit_id=models.   
         
         
# class testCategory(models.Model):
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

#     name=models.CharField(max_length=250)  
    
    
#     class MPTTMeta:
#         order_insertion_by = ['name']

#     def __str__(self):
#         return self.name  
    
    
# class testObject(models.Model):
#     name=models.CharField(max_length=250)
    
#     def __str__(self):
#         return self.name
       
    
# class test(models.Model):
#     name = models.CharField(max_length=250, null=True)    
#     category =  models.ForeignKey(testCategory, on_delete=models.CASCADE)
        
# class testParametor(models.model):
#     test_id= models.ForeignKey(test, on_delete=models.CASCADE)
#     name=models.CharField(max_length=250)
#     upper_limit=models.CharField(max_length=250)
#     lower_limit=models.CharField(max_length=250)
#     unit_id=models.IntegerField()



# class testCondition(models.Model):
        
    
        
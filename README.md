# PasswordGenerator

## About
We all make use of passwords on a daily basis, 
to keep your account safe and prevent your password from being hacked we have to make our password is hard enough that nobody can guess.
Password generator is a Random Password generating program which generates a password mix of upper and lowercase letters,
as well as numbers and symbols strong enough to provides great security.

## Modules Used
### Random module
Random module is used to perform the random generations. We are making use of random.sample module here. 
If you will observe in the output all characters will be unique. random.sample() never repeats characters. 
If you don’t want to repeat characters or digits in the random string,
then use random.sample() but it is less secure because it will reduce the probability of combinations because we are not allowing repetitive letters and digits.

def word_guessed():
	#if a letter is in the secret which hasn't been guessed, word_guessed is false
	for a in secret_word:
		if a not in letters_guessed:
			return False
	return True
def print_guessed():
	character_list=[]
	for a in secret_word:
		#add the letter to the character list if its in the secret word
		if a in letters_guessed:
			character_list.append(a)
		#if guess not in secret list, add a -
		else:
			character_list.append('-')
	print(''.join(character_list))

#can set this to whatever you want
secret_word='fireman'
letters_guessed=[]
mistakes=0
#set this to whatever you want
max_mistakes=6
#loop runs while mistakes are less than the max mistakes allowed
while mistakes < max_mistakes:
	print_guessed()
	print(f'You have guessed the following: {letters_guessed}\nyou have {max_mistakes-mistakes} mistakes left')
	guess=input('Guess a letter or word: Words will count as two mistakes for each wrong word\n')
	guess=guess.lower()
	
	#if the guess = secret word, done
	if guess==secret_word:
		print(f'Congratulations! You have guessed the secret word! The secret word was {secret_word}')
		break
	#check to see if guess has already been guessed
	if guess in letters_guessed:
		print('Oops, you have already guessed that! Try again')
		guess=input('Guess a word or a letter: ').lower()

	elif guess not in letters_guessed:
		#add guess to guess list
		letters_guessed.append(guess)
		#conditionals: check if the guess is in secret word or not, or if they have guessed a word and not a letter
		if guess in secret_word and len(guess)==1:

			#break loop if the word has been guessed and return a congratulatory message
			if word_guessed():
				print_guessed()
				print(f'Congratulations! You have guessed the secret word! The secret word was {secret_word}')
				break
			print(f'Nice guess! {guess} is in the secret word')
		#add two mistakes if they guess a word 
		elif len(guess) > 1:
			mistakes+=2
		#add one mistake if guess a letter
		else:
			mistakes+=1




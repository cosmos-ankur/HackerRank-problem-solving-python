grades = [38,33,64]

def ass_grad(grades):
	res = []
	for grade in grades:
		if (grade >= 38):
			mod5 = grade%5
			if mod5>3:
				grade += (5-mod5)
		res.append(grade)
	return res

print(ass_grad([37,44,69,72]))
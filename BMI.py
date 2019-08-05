height = float(input('請輸入您的身高cm：')) / 100
weight = int(input('請輸入您的體重kg：'))
BMI = weight / (height * height)
BMI = float(BMI)
if BMI < 18.5:
	print('您的BMI爲',BMI,'體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('您的BMI爲',BMI,'正常')
elif BMI >= 24 and BMI < 27:
	print('您的BMI爲',BMI,'過重')
elif BMI >= 27 and BMI < 30:
	print('您的BMI爲',BMI,'輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('您的BMI爲',BMI,'中度肥胖')
else:
	print('您的BMI爲',BMI,'重度肥胖')



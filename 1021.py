
#This function is generic and process entries and returns all it's arguments
def process_entry():
	entry = input()
	return float(entry)





class Change:
	rest = float
	
	notes_qnts = {
		100:int,
		50:int,
		20:int,
		10:int,
		5:int,
		2:int
	}

	coin_qnts = {
		1:int,
		0.5:int,
		0.25:int,
		0.10:int,
		0.05:int,
		0.01:int
	}

	def __init__(this):
		this.rest = 0
		for key in this.notes_qnts:
			this.notes_qnts[key] = 0
		for key in this.coin_qnts:
			this.coin_qnts[key] = 0
		

	def get_qnt(this, value, note_value):
		qnt = int(value // note_value)
		this.rest = value - note_value * qnt
		return qnt

	def set_all_qnts(this,initial_value):
		this.rest = initial_value
		for key in this.notes_qnts:
			this.notes_qnts[key] = this.get_qnt(this.rest, key)
		for key in this.coin_qnts:
			this.coin_qnts[key] = this.get_qnt(this.rest, key)
		
	def log_qnt(this, qnt, key, type):
		print(f'{qnt} {type}(s) de R$ {key:.2f}')

	def log_all_qnts(this):
		print('NOTAS:')
		for key in this.notes_qnts:
			qnt = this.notes_qnts.get(key)
			this.log_qnt(qnt, key, 'nota')	
		print('MOEDAS:')
		for key in this.coin_qnts:
			qnt = this.coin_qnts.get(key)
			this.log_qnt(qnt, key, 'moeda')	
		
entry = process_entry()

change = Change()
change.set_all_qnts(entry)
change.log_all_qnts()
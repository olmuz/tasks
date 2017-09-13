def vat_calc(sum, vat, vat_included):
	vat_to_float = vat/100
	if vat_included:
		value_without_vat = sum / (1 + vat_to_float)
		return sum, float(format(value_without_vat, '.2f')), vat
	else:
		value_with_vat = sum + sum * vat_to_float
		return float(format(value_with_vat, '.2f')), sum, vat
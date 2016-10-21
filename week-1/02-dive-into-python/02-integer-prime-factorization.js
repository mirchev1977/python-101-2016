





function prime_factorization(n) {
	let prime_numbers = [2, 3, 5, 7];
	let output = [];
	for(let divider of prime_numbers){
		let result = [];
		if (n % divider === 0) {
			result = recursion(n, divider, 0);
			n = result[0];
			let counter = result[1];
			let arr = [divider, counter];
			output.push(arr);
		}
	}

	if(n > 1){
		let counter = 1;
		let arr = [n, counter];
		output.push(arr);
	}
	

	return output;
}

console.log(prime_factorization(14));





function recursion(n, divider, counter){
	if (n % divider === 0) {
		n = n / divider;
		counter++;
		[n, counter] = recursion(n, divider, counter);
	}

	return [n, counter];
}
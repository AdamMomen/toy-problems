const minRemoveToMakeValid = (s) => {
	const forwardStack = []
	const backwardStack = []
	
	
}

const iterator = (string, direction, callback) => {
	let start = direction === 1? 0: string.length -1;
	let limit = direction === 1? string.length: 0;
	

	for(start; start < limit; direction ==1? start++ : start--) { 
		callback(string[start], start, string)
	}
}

const iterateForward = (string) => {
	iterator(string, 1, (e) => console.log(e))
}

let input = "a(b(c)"
console.log(
	iterateForward(	input )
)



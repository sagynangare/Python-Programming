var input_array;
input_array = {};
var i;
for (i = 0; i < 10; i++) {
    var random;
    random = rand(1, 100);
    array_push(input_array, random);
}
console.log('Unsorted array is: ');
console.log('<br />');
print_r(input_array);
var j;
for (j = 0; j < count(input_array); j++) {
    for (i = 0; i < count(input_array) - 1; i++) {
        if (input_array[i] > input_array[i + 1]) {
            var temp;
            temp = input_array[i + 1];
            input_array[i + 1] = input_array[i];
            input_array[i] = temp;
        }
    }
}
console.log('Sorted Array is: ');
console.log('<br />');
print_r(input_array);

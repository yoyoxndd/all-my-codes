let count = 0;

document.getElementById("increase").addEventListener("click", function() {
    count++;
    document.getElementById("count").textContent = count;
});

document.getElementById("decrease").addEventListener("click", function() {
    count--;
    document.getElementById("count").textContent = count;
});

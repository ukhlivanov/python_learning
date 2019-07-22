name = 'GLOBAL'

function tmp(){
    name = 'ENCLOSED'
        function tmp1() {
            name = 'LOCAL'
            console.log(name)
        }
        tmp1()
}

tmp()
console.log(name)
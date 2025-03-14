function isAnagram(s:string, t: string) {
 let countS   = new Map()
 let countT = new Map()

 if(s.length != t.length){
    return false
 }
    for(const i of s){
        countS[i] = (countS[i] || 0) + 1
    }
    
    for(const i of t){
        countT[i] = (countT[i] || 0) + 1
    }

    console.log(countS)
    console.log(countT)

    for(const i of s){
        if(countS[i] != countT[i]){
            return false
        }
        // console.log(countS[i])
        // console.log(countT[s[i]])
        
    }
    return true
}

const s = "rata"
const t = "arat"
console.log(isAnagram(s, t))
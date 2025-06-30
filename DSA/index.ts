function isAnagram(s: string, t: string) {
  let countS = new Map();
  let countT = new Map();

  if (s.length != t.length) {
    return false;
  }
  for (const i of s) {
    countS[i] = (countS[i] || 0) + 1;
  }

  for (const i of t) {
    countT[i] = (countT[i] || 0) + 1;
  }

  console.log(countS);
  console.log(countT);

  for (const i of s) {
    if (countS[i] != countT[i]) {
      return false;
    }
  }
  return true;
}

const s = 'rata';
const t = 'arat';

function twoSum(arr, target) {
  const storage = new Map<number, number>();
  for (let index = 0; index < arr.length; index++) {
    const num = arr[index];
    const neededValue = target - num;
    if (storage.has(neededValue)) {
      return [storage.get(neededValue), index];
    }
    storage.set(num, index);
  }
  return [];
}

// console.log(twoSum([2, 7, 11, 15], 9));

function longestCommonPrefix(strs) {
  let ans = '';

  for (let i = 0; i < strs[0].length; i++) {
    for (let j = 0; j < strs.length; j++) {
      if (i == strs[j].length || strs[j][i] != strs[0][i]) {
        return ans;
      }
    }
    ans += strs[0][i];
  }
  return ans;
}

// const strs = [''];
// console.log(longestCommonPrefix(strs));

// function groupAnagrams(strs: string[]){
//   const res = new Map<string, string[]>()
//   for(let s of strs){
//     const sortedS = s.split('').sort().join('')
//     if(!res.has(sortedS)) {
//       res.set(sortedS, [])
//     }
//     res.get(sortedS)?.push(s)
//   }
//   return Array.from(res.values())
// }
function groupAnagrams(strs: string[]) {
  const res = new Map<string, string[]>();

  for (let s of strs) {
    const count = Array(26).fill(0);
    for (let c of s) {
      count[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
    }
    const newArray = res.get(count.toString()) || [];
    newArray?.push(s);
    res.set(count.toString(), newArray);
  }
  return Array.from(res.values());
}

const strs = ['act', 'pots', 'tops', 'cat', 'stop', 'hat'];

// console.log(groupAnagrams(strs));

function removeElement(nums: number[], val: number) {
  let k = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != val) {
      nums[k] = nums[i];
      k += 1;
    }
  }
  return k;
}

// function majorityElement(nums) {
//   const hash = new Map()
//   let res = 0
//   let max_num = 0
//   for(let i of nums) {
//     hash.set(i, (hash.get(i) || 0)  + 1)
//     res = hash.get(i) > max_num ? i : res
//     max_num = Math.max(hash.get(i), max_num)
//   }
// return res
//
// }
//

function majorityElement(nums) {
  let res = 0;
  let count = 0;

  for (let i of nums) {
    if (count == 0) {
      res = i;
    }
    count += res == i ? +1 : -1;
  }
  return res;
}

const nums = [6, 5, 5];
// console.log(majorityElement(nums))

class MyHashSet {
  private data: number[];

  constructor() {
    this.data = [];
  }

  add(key: number) {
    return this.data.includes(key) ? '' : this.data.push(key);
  }

  remove(key: number) {
    return this.data.splice(this.data.indexOf(key), 1);
  }

  contains(key: number) {
    return this.data.includes(key);
  }
}

const obj = new MyHashSet();
obj.add(33);

function sortArray(nums) {
  mergeSort(nums, 0, nums.length);
  return nums;
}

function mergeSort(arr, l, r) {
  if (l == r) return;
  let m = Math.floor((l + r) / 2);
  mergeSort(arr, l, m);
  mergeSort(arr, m + 1, r);
  merge(arr, l, m, r);
  return arr;
}
function merge(arr, l, m, r) {
  let i = l;
  let j = 0;
  let k = 0;
  const left = arr.slice(l, m + 1);
  const right = arr.slice(m + 1, r + 1);
  while (j < left.length && k < right.length) {
    if (left[j] < right[k]) {
      arr[i] = left[j];
      j += 1;
      i += 1;
    } else {
      arr[i] = right[k];
      k += 1;
      i += 1;
    }
  }
  while (j < left.length) {
    arr[i] = left[j];
    j += 1;
    i += 1;
  }
  while (k < right.length) {
    arr[i] = right[k];
    k += 1;
    i += 1;
  }
}

const arr = [23, 432, 238, 2];  
console.log(mergeSort(arr, 0, arr.length));




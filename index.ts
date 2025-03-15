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
    for (let j = 0 ; j < strs.length; j++) {
      if (i == strs[j].length || strs[j][i] != strs[0][i]) {
        return ans;
      } 
    }
    ans += strs[0][i];
  }
  return ans;
}

const strs = ['']; 
console.log(longestCommonPrefix(strs));

import fs from 'fs';

const FILE_PATH = './data/memo.json'

const getData = () => {
    const f = fs.readFileSync('./data/memo.json', 'utf-8');
    return JSON.parse(f)
    // return arr = data.list
}

const setData = (data) => {
    fs.writeFileSync('./data/memo.json', JSON.stringify(data), 'utf-8');
}

export const list = () => {
    console.log("words.list()")
    const arr = getData();
    for(const v of arr.list) console.log(v);
}
export const insert = (word) => {
    console.log("words.insert()", word)
    const data = getData();
    const id = (data.list.length === 0 ? 1 : data.list.at(-1).id + 1)
    data.list.push({id, word})
    console.log(data)
    setData(data)
}
export const remove = (id) => {
    const data = getData(); 
    data.list = data.list.filter( v => v.id != id )
    console.log("words.remove()", id)
    setData(data)
}
export const update = (id, word) => {
    const data = getData();
    data.list = data.list.filter(v => {
        if(v.id == id) v.word = word
        return v
    })
    console.log("words.update()", id, word, data)
    setData(data)
}
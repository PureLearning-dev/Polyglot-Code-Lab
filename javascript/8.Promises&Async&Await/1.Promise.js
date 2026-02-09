/*  promise是为了将异步操作代码的传统写法改为更加优雅的一种机制。
 *  传统写法容易出现“回调地狱”，而promise提供的机制可以将回调函数改为与同步函数类似的格式。
 *
 *  Promise可以通过构造函数的形式创建，其接收一个函数，此函数接收两个函数参数，分别是用于执行成功和执行失败的两种情况。
 *  自动返回在两个函数参数中传入的数据并将这个数据包裹在promise中。
 */
let tag = true;

let promise = new Promise((resolved, rejected)=>{
    if(tag){
        resolved("成功执行promise后返回的结果：成功执行！");
    }else{
        rejected("失败后的信息：执行失败！");
    }
})

console.log(promise);

promise.then((message)=>{
    console.log("在promise成功执行时执行此方法" + message);
}).catch((error)=>{
    console.log(error);
})


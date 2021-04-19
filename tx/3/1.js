// 1
const checkQQEmail = {
  init(param) {
    const that = this;
    const input = param.input;
    const output = param.output;
    if (!input || !output) return;
    input.blur = _blur;
    // TODO: 请为input绑定blur事件，回调函数为_blur

    function _blur() {
      // TODO: 请获取input当前的值
      const val = input.value;
      const content = "";
      const emails = that.getItems(content);
      // TODO: 请筛选出错误的emails中错误的QQ邮箱
      const error = email.filter((x) => !isQQEmail(x));
      const map = {};
      error.forEach((item) => (map[item] = true));
      const right = emails.filter((item) => {
        // TODO: 请判断item是否重复出现过
        const isExist = false;
        if (map[item]) {
          isExist = true;
        }
        map[item] = true;
        // TODO: 请填写正确的返回值，替换false
        return isExist;
      });
      input.value = right.join("\n");
      // TODO: 请将数组right通过 \n 拼接，然后赋值给input节点
      output.value = error.join("\n");
      // TODO: ��将数组error通过 \n 拼接，然后赋值给output节点
    }
  },
  getItems(content) {
    // TODO: 请根据题目中给定的分隔符，将content分割成字符串数组，请去掉数组中的空白字符项
    return content.split("\n");
  },
  /**
   *
   * @param {string} email
   * @returns Boolean
   */
  isQQEmail(email) {
    // TODO: 请判断email是否是正确的QQ邮箱
    if (!email.endsWith("@qq.com")) {
      return false;
    }
    parseInt(email.slice(0, email.length - "@qq.com".length));
    return true;
  },
};

checkQQEmail.init({
  // TODO: 请获取class=input的节点
  input: document.getElementsByClassName("input")[0],
  // TODO: 请获取class=output的节点
  output: document.getElementsByClassName("output")[0],
});

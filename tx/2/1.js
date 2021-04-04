// 日常不会做
const autosize = {
  bakEl: null,
  init(textarea) {
    const that = this;
    if (!textarea) return;

    // TODO: 请获取textarea的高度，并替换下面的null值
    const height = parseFloat(textarea.scrollHeight);
    // TODO: 请获取textarea的padding-top和padding-bottom值，并分别替换下面的null值
    const padding = parseFloat(null) + parseFloat(null);
    // TODO: 请将textarea溢出元素内容区的内容设置为不可见
    // TODO: 请为textarea绑定input事件，回调函数为_change
    // TODO: 请为textarea绑定click事件，回调函数为_change
    textarea.input = _change;
    textarea.click = _change;
    _change();
    return _change;

    function _change() {
      const bakEl = that.copy(textarea, that.bakEl);
      that.bakEl = bakEl;
      bakEl = textarea;
      // TODO: 请将textarea的值赋值给bakEl
      // TODO: 请将bakEl的高度设置成 height px
      // TODO: 请在页面body节点中插入bakEl节点
      let val = bakEl.scrollHeight - padding;
      val <= height && (val = height);
      // TODO: 请将textarea的高度设置成 val px
      textarea.style.height = `${val}px`;
      // TODO: 请在页面body节点中移除bakEl节点
    }
  },
  copy(el, bak) {
    const attr = [
      "direction",
      "boxSizing",
      "width",
      "height",
      "overflowX",
      "overflowY",
      "borderTopWidth",
      "borderRightWidth",
      "borderBottomWidth",
      "borderLeftWidth",
      "borderStyle",
      "paddingTop",
      "paddingRight",
      "paddingBottom",
      "paddingLeft",
      "fontStyle",
      "fontVariant",
      "fontWeight",
      "fontStretch",
      "fontSize",
      "fontSizeAdjust",
      "lineHeight",
      "fontFamily",
      "textAlign",
      "textTransform",
      "textIndent",
      "textDecoration",
      "letterSpacing",
      "wordSpacing",
      "resize",
      "tabSize",
      "MozTabSize",
    ];
    bak = bak || el.cloneNode();
    const style = bak.style;
    const computed = this.style(el);
    style.position = "absolute";
    style.visibility = "hidden";
    // TODO: 请将computed中所有的attr的样式复制到style中
    return bak;
  },
  style(el) {
    return window.getComputedStyle(el);
  },
};
// TODO: 请获取class=editor的节点，并替换下面的null值
autosize.init(document.getElementsByClassName("editor"));

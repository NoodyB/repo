// Progressive enhancement: add "Copy" buttons to prompt/code blocks.
(function () {
  if (!navigator.clipboard) return;
  document.querySelectorAll(".prose pre").forEach(function (pre) {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "copy-btn";
    btn.textContent = "Copy";
    btn.setAttribute("aria-label", "Copy this text to the clipboard");
    btn.addEventListener("click", function () {
      var code = pre.querySelector("code");
      navigator.clipboard.writeText((code || pre).innerText).then(function () {
        btn.textContent = "Copied";
        setTimeout(function () { btn.textContent = "Copy"; }, 1800);
      });
    });
    pre.appendChild(btn);
  });
})();

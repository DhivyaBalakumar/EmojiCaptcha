document.addEventListener("DOMContentLoaded", () => {
    const captchaBox = document.querySelector(".captcha-box");
    const emojis = document.querySelectorAll(".emoji");

    emojis.forEach(emoji => {
        emoji.addEventListener("click", () => {
            let correctEmoji = "😠"; // Set correct emoji for now
            if (emoji.textContent === correctEmoji) {
                captchaBox.classList.remove("wrong");
                captchaBox.classList.add("correct");
            } else {
                captchaBox.classList.remove("correct");
                captchaBox.classList.add("wrong");
            }
        });
    });
});

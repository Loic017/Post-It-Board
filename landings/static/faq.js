const faqHeads = document.querySelectorAll(".faq-head");
const faqContents = document.querySelectorAll(".faq-content");

faqHeads.forEach((faqHead, index) => {
    faqHead.addEventListener("click", () => {
        console.log("hello");
        faqContents[index].classList.toggle("hidden");
        faqHead.classList.toggle("faq-head-clicked");
        faqHead.classList.toggle("faq-head");
        for (let i = 0; i < faqContents.length; i++) {
            if (i !== index) {
                faqContents[i].classList.toggle("hidden");
                faqHeads[i].classList.toggle("faq-head");
                faqHeads[i].classList.toggle("faq-head-clicked");
            }
        }
    });
});

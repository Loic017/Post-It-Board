const faqHeads = document.querySelectorAll(".faq-head");
const faqContents = document.querySelectorAll(".faq-content");

faqHeads.forEach((faqHead, index) => {
    faqHead.addEventListener("click", () => {
        console.log("hello");
        faqContents[index].classList.toggle("hidden");
        faqHead.classList.toggle("faq-head-clicked");
        faqHead.classList.toggle("faq-head");
    });
});

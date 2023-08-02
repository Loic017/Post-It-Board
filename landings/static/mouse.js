const pricingFronts = document.querySelectorAll(".pricing-button");
const pricingBacks = document.querySelectorAll(".back");

pricingFronts.forEach((pricingFront, index) => {
    pricingFront.addEventListener("click", () => {
        pricingFronts[index].classList.add("hidden");
        pricingBacks[index].classList.remove("hidden");
    });
});

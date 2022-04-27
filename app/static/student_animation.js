const submit_button_animation = () => {
    const student_form = document.querySelector("form");
    const btn = document.querySelector(".submit-btn");
    student_form.addEventListener("submit", () => {
        const tl = gsap.timeline();
        tl.to("i", {rotate: "20deg", duration: 1.5, ease: "power3.out"})
          .to("i", {repeat:-1, y: 1, yoyo: true, duration: 2, ease: Back.easeInOut.config(25)});
        btn.value = "             Loading...";
    });
}

submit_button_animation();
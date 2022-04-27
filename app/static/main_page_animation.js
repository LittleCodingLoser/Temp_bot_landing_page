gsap.registerPlugin(ScrollTrigger);

const loading_animation = () => {
    const topic = document.querySelector("h1"),
          bot = document.querySelector(".bot-says-hi"),
          tl = gsap.timeline();

    tl.from(topic, {y: -30, color: "transparent", duration: 0.5, ease: "power1.out"})
      .from(bot, {x: 50, opacity: 0, duration: 1.5, ease: "power3.out"})
}

const description_animation = () => {
      const text = document.querySelector(".description-text"),
            bot = document.querySelector(".temp-bot-feature"),
            mail = document.querySelector(".mail"),
            file = document.querySelector(".file"),
            rocket = document.querySelector(".rocket"),
            gear = document.querySelector(".gear"),
            tl = gsap.timeline();
      
      ScrollTrigger.create({
        trigger: text,
        animation: tl,
        start: 'top 60%',
        toggleActions: "restart resume resume reverse",
        duration: 0.5, 
        ease: "power3.out" 
      });

      tl.from(text, {x: -5, opacity: 0})
        .from(gear, {x: 5, opacity: 0})
        .from(bot, {y: 5, opacity: 0}, "-=0.2")
        .from(mail, {x: 5, opacity: 0})
        .from(file, {x: -5, opacity: 0})
        .from(rocket, {x: -5, opacity: 0});
}

const health_leader_instruction_animation = () => {
      const topic = document.querySelector(".health_leader h2"),
            text = document.querySelector(".health_leader p"),
            link = document.querySelector(".health_leader button p"),
            icon = document.querySelector(".health_leader .circle"),
            tl = gsap.timeline();
      
      ScrollTrigger.create({
        trigger: topic,
        animation: tl,
        start: 'top 60%',
        toggleActions: "restart resume resume reverse",
        duration: 0.5, 
        ease: "power3.out" 
      });

      tl.from(topic, {x: -5, opacity: 0})
        .from(text, {x: -5, opacity: 0}, "-=0.5")
        .from(link, {x: -5, opacity: 0}, "-=1")
        .from(icon, {y: -10, rotation: "90deg", opacity: 0});
}

const student_instruction_animation = () => {
      const topic = document.querySelector(".student h2"),
            text = document.querySelector(".student p"),
            link = document.querySelector(".student button p"),
            icon = document.querySelector(".student .circle"),
            tl = gsap.timeline();
      
      ScrollTrigger.create({
        trigger: topic,
        animation: tl,
        start: 'top 60%',
        toggleActions: "restart resume resume reverse",
        duration: 0.5, 
        ease: "power3.out" 
      });

      tl.from(topic, {x: -5, opacity: 0})
        .from(text, {x: -5, opacity: 0}, "-=0.5")
        .from(link, {x: -5, opacity: 0}, "-=1")
        .from(icon, {y: -10, rotation: "90deg", opacity: 0});
}

loading_animation()
health_leader_instruction_animation()
student_instruction_animation()
description_animation()
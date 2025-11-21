setTimeout(() => {
    const el = document.getElementById("messages");
    if (el) {
        el.style.transition = "opacity 0.6s";
        el.style.opacity = "0";

        // Opcional: quitarlo del flujo después del fadeOut
        setTimeout(() => el.style.display = "none", 600);
    }
}, 5000);
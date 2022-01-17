const swallAlerts =(message,type,position,duration,showConfirmButton)=>{
    const Toast = Swal.mixin({
        toast: true,
        position: position,
        showConfirmButton: showConfirmButton,
        timer: duration,
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer)
          toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
      })
      
      Toast.fire({
        icon: type,
        title: message,
        
      })
};
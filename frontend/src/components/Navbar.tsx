const Navbar = () => {
  return (
    <nav className="bg-slate-900 py-4 px-8 flex justify-between items-center sticky top-0 z-50 border-b border-slate-800">
      {/* Logo */}
      <div className="text-2xl font-bold text-white tracking-tight">
        Ecua<span className="text-sky-400">Trade</span>
      </div>

      {/* Links */}
      <ul className="hidden md:flex space-x-8 text-sm font-medium text-slate-400">
        <li className="hover:text-white cursor-pointer transition-colors duration-200">Inicio</li>
        <li className="hover:text-white cursor-pointer transition-colors duration-200">Productos</li>
        <li className="hover:text-white cursor-pointer transition-colors duration-200">Ofertas</li>
        <li className="hover:text-white cursor-pointer transition-colors duration-200">Contacto</li>
      </ul>

      {/* Carrito */}
      <button className="bg-sky-400 text-slate-900 px-5 py-2 rounded-lg text-sm font-semibold hover:bg-sky-300 transition-colors duration-200 flex items-center gap-2">
        <svg xmlns="http://www.w3.org/2000/svg" className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
          <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
        </svg>
        Carrito (0)
      </button>
    </nav>
  );
};

export default Navbar;

import { useState } from "react";
import { Search, User, ShoppingCart, ChevronDown } from "lucide-react";

const megaMenu = [
  {
    titulo: "Periféricos",
    items: ["Mouse", "Teclados", "Headsets", "Micrófonos", "Webcams"],
  },
  {
    titulo: "Componentes",
    items: ["Monitores", "Cases", "Bases Cooler", "Soportes"],
  },
  {
    titulo: "Accesorios",
    items: ["Mouse Pads", "Gamepads", "Keycaps", "Switches", "Figuras"],
  },
  {
    titulo: "Gamer & Más",
    items: ["Consolas", "Videojuegos", "Sillas", "Combos", "Promociones"],
  },
];

const Navbar = () => {
  const [menuAbierto, setMenuAbierto] = useState(false);
  const [busqueda, setBusqueda] = useState("");

  return (
    <nav className="bg-slate-900 sticky top-0 z-50 border-b border-slate-800">
      {/* Fila principal */}
      <div className="px-8 py-3 flex items-center gap-6">
        {/* Logo */}
        <div className="text-xl font-bold text-white tracking-tight flex-shrink-0">
          Ecua<span className="text-sky-400">Trade</span>
        </div>

        {/* Barra de búsqueda */}
        <div className="flex-1 flex items-center bg-white rounded-lg overflow-hidden max-w-2xl">
          <input
            type="text"
            value={busqueda}
            onChange={(e) => setBusqueda(e.target.value)}
            placeholder="Busca en más de 10,000 productos..."
            className="flex-1 px-4 py-2 text-sm text-slate-700 outline-none"
          />
          <button className="bg-sky-400 hover:bg-sky-300 transition-colors px-4 py-2 flex items-center justify-center">
            <Search className="w-4 h-4 text-slate-900" />
          </button>
        </div>

        {/* Acciones derecha */}
        <div className="flex items-center gap-3 flex-shrink-0 ml-auto">
          <button className="flex items-center gap-2 text-slate-400 hover:text-white transition-colors text-sm">
            <User className="w-4 h-4" />
            <span className="hidden lg:inline">Mi cuenta</span>
          </button>

          <button className="bg-sky-400 hover:bg-sky-300 transition-colors text-slate-900 px-4 py-2 rounded-lg text-sm font-semibold flex items-center gap-2">
            <ShoppingCart className="w-4 h-4" />
            Carrito (0)
          </button>
        </div>
      </div>

      {/* Fila de links */}
      <div className="px-8 py-2 flex items-center gap-8 border-t border-slate-800 text-sm">
        <a className="text-slate-400 hover:text-white cursor-pointer transition-colors">
          Inicio
        </a>

        {/* Productos con mega menú */}
        <div
          className="relative"
          onMouseEnter={() => setMenuAbierto(true)}
          onMouseLeave={() => setMenuAbierto(false)}
        >
          <button className="flex items-center gap-1 text-slate-400 hover:text-white transition-colors">
            Productos
            <ChevronDown
              className={`w-3 h-3 transition-transform duration-200 ${menuAbierto ? "rotate-180" : ""}`}
            />
          </button>

          {/* Mega menú desplegable */}
          {menuAbierto && (
            <div className="absolute top-full left-0 mt-2 w-[560px] bg-slate-800 border border-slate-700 rounded-xl shadow-2xl p-6 grid grid-cols-4 gap-6 z-50">
              {megaMenu.map((col) => (
                <div key={col.titulo}>
                  <p className="text-sky-400 text-xs font-semibold uppercase tracking-wider mb-3">
                    {col.titulo}
                  </p>
                  <ul className="space-y-2">
                    {col.items.map((item) => (
                      <li
                        key={item}
                        className="text-slate-400 hover:text-white text-sm cursor-pointer transition-colors"
                      >
                        {item}
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          )}
        </div>

        <a className="text-slate-400 hover:text-white cursor-pointer transition-colors">
          Ofertas
        </a>
        <a className="text-slate-400 hover:text-white cursor-pointer transition-colors">
          Contacto
        </a>
      </div>
    </nav>
  );
};

export default Navbar;